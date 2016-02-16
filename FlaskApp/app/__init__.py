from flask import Flask, render_template, redirect, url_for, request
app = Flask(__name__)
from app import views
# all init should goes here file settings db settings