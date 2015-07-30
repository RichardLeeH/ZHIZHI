# -*- coding: utf-8 -*-

from flask import (Blueprint, render_template, g, request, url_for,
                   current_app, send_from_directory, json, redirect,
                   make_response, abort)

frontend = Blueprint('frontend', __name__, template_folder="templates",
                     url_prefix='/')
import time
from search import do_search

PAGE_SIZE = 10


@frontend.route('/')
def index():
    return render_template('index.html')


@frontend.route('search/')
def search():
    query = request.args.get('q')
    if 'page' in request.args:
        page = request.args['page']
    else:
        page = 1
    start = time.time()

    search_res = do_search(query, page)
    total_hits = search_res["total"]
    # results = [each["_source"] for each in search_res["hits"]]
    results = []
    for each in search_res["hits"]:
        each["_source"]["people"] = each["_source"]["people_link"].split("/")[-1].split("?")[0] if each["_source"]["people_link"] else u"匿名"
        for highlight in each["highlight"].keys():
            each["_source"][highlight] = each["highlight"][highlight][0]
        results.append(each["_source"])
    end = time.time()
    total_page = total_hits / PAGE_SIZE
    if total_page < 10:
        page_list = range(1, total_page)
    elif int(page) + 10 < total_page:
        page_list = range(int(page), int(page) + 10)
    else:
        page_list = range(page, total_page)
    next_page = 0 if int(page) + 1 >= total_page else int(page) + 1
    return render_template('res_search.html', data={'results': results,
                                                    'query': query,
                                                    'count': total_hits,
                                                    'time': end - start,
                                                    'page': page,
                                                    'total_page': total_page or 1,
                                                    'page_list': page_list,
                                                    'previous_page': int(
                                                        page) - 1,
                                                    'next_page': next_page})


@frontend.route('/robots.txt')
def static_from_root():
    # Static items
    return send_from_directory(current_app.static_folder, request.path[1:])


@frontend.route('/favicon.ico')
def favicon():
    return redirect('/static/favicon.png')
