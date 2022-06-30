from app import app
from flask import render_template, request, redirect, url_for
from googletrans import Translator
from bs4 import BeautifulSoup
import requests
import json
import os
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt



dest = "en"
src = "pl"
translator = Translator()

def get_element(parent, selector, attribute = None, return_list = False):
    try:
        if return_list:
            return ", ".join([item.text.strip() for item in parent.select(selector)])
        if attribute:
            return parent.select_one(selector)[attribute]
        return parent.select_one(selector).text.strip()
    except (AttributeError, TypeError):
        return None

def translate(text, src=src, dest=dest):
    try:
        return translator.translate(text, src=src, dest=dest).text
    except (AttributeError, TypeError):
        print("Error")
        return ""

opinion_elements = {
    "author":["span.user-post__author-name"],
    "rcmd": ["span.user-post__author-recomendation > em"],
    "score": ["span.user-post__score-count"],
    "content": ["div.user-post__text"],
    "posted_on": ["span.user-post__published > time:nth-child(1)", "datetime"],
    "bought_on": ["span.user-post__published > time:nth-child(2)", "datetime"],
    "useful_for": ["button.vote-yes > span"],
    "useless_for": ["button.vote-no > span"],
    "pros": ["div.review-feature__title--positives ~ div.review-feature__item", None, True],
    "cons": ["div.review-feature__title--negatives ~ div.review-feature__item", None, True]
}

@app.route('/')
def index():
    name = "Arsenii Ion"
    return render_template("index.html.jinja")

@app.route('/author')
def author():
    return render_template("author.html.jinja")

@app.route('/extract')
def extract():
    return render_template("extract.html.jinja")

@app.route('/products')
def products():
    products = [filename.split(".")[0] for filename in os.listdir("app/opinions")]
    return render_template("products.html.jinja", products=products)

@app.route('/product/<product_id>')
def product(product_id):
    opinions = pd.read_json(f"app/opinions/{product_id}.json")
    stats={
        "opinions_count": len(opinions),
        "pros_count": opinions["pros"].map(bool).sum(),
        "cons_count": opinions["cons"].map(bool).sum(),
        "average_score": opinions["score"].mean().round(2)
    }
    if not os.path.exists("app/static/plots"):
        os.makedirs("app/static/plots")
    recommendations = opinions["rcmd"].value_counts(
        dropna=False).sort_index().reindex([False, True, None])
    recommendations.plot.pie(
        label = "",
        title = "Recommendations: "+product_id,
        labels = ["Not recommend", "Recommend", "No opinion"],
        colors = ["crimson", "forestgreen", "grey"],
        autopct = lambda p: f"{p:.1f}%" if p>0 else ""
    )
    plt.savefig(f"app/static/plots/{product_id}_rcmd.png")
    plt.close()
    stars = opinions["score"].value_counts(
        dropna=False).sort_index().reindex(np.arange(0,5.5,0.5))
    stars.plot.bar(
        label = "",
        title = "Stars score: "+product_id,
        xlabel = "Stars values",
        ylabel = "Opinions count",
        color = "hotpink",
        rot = 0
    )
    plt.savefig(f"app/static/plots/{product_id}_stars.png")
    plt.close()
    return render_template("product.html.jinja", product_id=product_id, stats=stats, opinions=opinions)

@app.route('/opinions', methods=["POST"])
def opinions():
    product_id = request.form.get("product_id")
    url = f"https://www.ceneo.pl/{product_id}#tab=reviews"
    all_opinions = []
    while (url):
        print(url)
        response = requests.get(url)
        page_dom = BeautifulSoup(response.text, "html.parser")
        opinions = page_dom.select("div.js_product-review")
        for opinion in opinions:
            single_opinion = {
                key: get_element(opinion, *values)
                for key, values in opinion_elements.items() 
            }
            single_opinion["opinion_id"] = opinion["data-entry-id"]
            single_opinion["rcmd"] = True if single_opinion["rcmd"] == "Polecam" else False if single_opinion["rcmd"] == "Nie polecam" else None
            single_opinion["score"] = float(single_opinion["score"].split("/")[0].replace(",", "."))
            single_opinion["useful_for"] = int(single_opinion["useful_for"])
            single_opinion["useless_for"] = int(single_opinion["useless_for"])
            single_opinion["content_en"] = translate(single_opinion["content"]) if single_opinion["content"] else ""
            single_opinion['pros_en'] = translate(single_opinion['pros']) if single_opinion["pros"] else ""
            single_opinion['cons_en'] = translate(single_opinion['cons']) if single_opinion["cons"] else ""
            all_opinions.append(single_opinion)
        try:
            url = "https://www.ceneo.pl"+get_element(page_dom,"a.pagination__next","href")
        except TypeError: 
            url = None
    if not os.path.exists("app/opinions"):
        os.makedirs("app/opinions")
    with open(f"app/opinions/{product_id}.json", "w", encoding="UTF-8") as jf:
        json.dump(all_opinions, jf, indent=4, ensure_ascii=False)
    return redirect(url_for("product", product_id=product_id))