from app import app
from app.models import *
from app import db
from flask import Flask, render_template, redirect,request,url_for
import os



@app.route('/')
def index():
    navs=NavbarInfo.query.all()
    sliders=NavbarSlider.query.all()
    icons=NavbarIcon.query.all()
    menus=NavbarMenu.query.all()
    aboutheads=AboutHeading.query.all()
    posts=AboutImg.query.all()
    aboutexts=About.query.all()
    lists=AboutList.query.all()
    txts=AboutEnd.query.all()
    clientheads=ClientHeading.query.all()
    logos=ClientImg.query.all()
    numbers=Testimional.query.all()
    servicesheads=ServivesHeading.query.all()
    blogs=Servives.query.all()
    ports=PortHeading.query.all()
    links=Portfolio.query.all()
    contacts=ContactHeading.query.all()
    endicons=ContactMe.query.all()
    socials=SocialIcon.query.all()
    return render_template('main/index.html',navs=navs,sliders=sliders,icons=icons,menus=menus,aboutheads=aboutheads,posts=posts,lists=lists,aboutexts=aboutexts,txts=txts,numbers=numbers,contacts=contacts,endicons=endicons,ports=ports
    ,links=links,servicesheads=servicesheads,blogs=blogs,socials=socials,logos=logos,clientheads=clientheads)
  
@app.route('/admin/contactform', methods=['GET','POST']) 
def contactform():
   contactforms =Contact.query.all()
   if request.method=='POST':
      contactform=Contact(
      user_name=request.form['user_name'],
      user_email=request.form['user_email'],
      user_message=request.form['user_message']
      )     
      db.session.add(contactform)
      db.session.commit()
      return redirect('/')
   return  render_template('admin/contactform.html',contactforms=contactforms )
   
@app.route("/admin/contactformdelete/<id>")
def contactformdelete(id):
   contactform =Contact.query.get(id)
   db.session.delete(contactform)
   db.session.commit()
   return redirect('/admin/contactform')



 
   