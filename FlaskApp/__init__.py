from flask import Flask, render_template, redirect, url_for, request
app = Flask(__name__)
from app import views