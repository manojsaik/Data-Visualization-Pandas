from flask import Flask,render_template, redirect, request, url_for, flash,abort, send_from_directory , session
import os
import pandas as pd
from datetime import timedelta
from openpyxl import load_workbook

piechart = Flask(__name__)


@piechart.route('/')
def home():
    basedir = os.path.abspath(os.path.dirname(__file__))
    ser=pd.read_excel(os.path.join(basedir,'servers.xlsx'))
    c=0;nc=0;
    for i in ser['Dat']:
        
        if i>=3.4:
            
            c=c+1
    
    nc=ser['Dat'].count()-c
    t=nc+c;
    pc=round((c/t)*100,2)
    print(c,nc)
    return render_template('site.html',c=c,nc=nc,t=t,pc=pc)

if __name__ == '__main__':
    piechart.run(debug=True)
