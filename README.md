Lyrics Crawler
======


Overview
========

A crawler made with Scrapy that crawls the lyrics for all songs of a given band.

Currently the crawler data source is [Vagalume](https://www.vagalume.com.br).

Requirements
============

* Python Python 3.6+
* Works on Linux, Windows, Mac OSX, BSD
* [Scrapy](https://github.com/scrapy/scrapy)

Installing and Executing
=======

    pip install scrapy
    python vagalume_band_crawler.py band_home page

The results will be saved into the data folder, with one tsv with all the song names and links and a json with song names, their respective album and lyrics.

Example
=======
The bands home page is usually just the band name with dashes `-` instead of spaces.

    python vagalume_band_crawler.py https://www.vagalume.com.br/green-day/
