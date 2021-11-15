from app import app
from app.models import *
from app import db
from flask import render_template,request,redirect
from flask import url_for
import os
# from flask_bcrypt import Bcrypt
def loginCheck(param):
    adminLoginStat = request.cookies.get('adminLoginStatus')
    if adminLoginStat=='beli':
        return param
    else:
        return redirect(url_for('login'))


@app.route('/admin')
def admin_index():
    navs=NavbarInfo.query.all()
    sliders=NavbarSlider.query.all()
    icons=NavbarIcon.query.all()
    menus=NavbarMenu.query.all()
    aboutheads=AboutHeading.query.all()
    posts=AboutImg.query.all()
    aboutexts=About.query.all()
    lists=AboutList.query.all()
    txts=AboutEnd.query.all()
    numbers=Testimional.query.all()
    clientheads=ClientHeading.query.all()
    logos=ClientImg.query.all()
    servicesheads=ServivesHeading.query.all()
    blogs=Servives.query.all()
    ports=PortHeading.query.all()
    links=Portfolio.query.all()
    contacts=ContactHeading.query.all()
    endicons=ContactMe.query.all()
    socials=SocialIcon.query.all()
    return loginCheck(render_template ('admin/index.html',navs=navs,sliders=sliders,icons=icons,menus=menus,aboutheads=aboutheads,posts=posts,lists=lists,aboutexts=aboutexts,txts=txts,numbers=numbers,contacts=contacts,endicons=endicons,ports=ports
    ,links=links,servicesheads=servicesheads,blogs=blogs,socials=socials,logos=logos,clientheads=clientheads))
  
# Navbar Info
@app.route('/admin/navbar', methods=['GET','POST']) 
def navbarinfo():
   navs=NavbarInfo.query.all() 
   if request.method=='POST':
      nav=NavbarInfo(
      navbar_icon=request.form['navbar_icon'],   
      navbar_icon_name=request.form['navbar_icon_name'],
      navbar_icon_txt=request.form['navbar_icon_txt'],
      navbar_icon_url=request.form['navbar_icon_url']

      )     
      db.session.add(nav)
      db.session.commit()
      return redirect('/admin/navbar')
   return loginCheck(render_template('admin/navbar.html',navs=navs))
   
   
@app.route("/admin/navbardelete/<id>")
def navbarinfodelete(id):
   nav=NavbarInfo.query.get(id)
   db.session.delete(nav)
   db.session.commit()
   return redirect('/admin/navbar')

@app.route("/admin/navbarupdate/<id>" , methods=['GET','POST'])  
def navbarupdate(id):
    nav=NavbarInfo.query.get(id)
    if request.method=='POST':
      nav.navbar_icon=request.form['navbar_icon']
      nav.navbar_icon_name=request.form['navbar_icon_name']
      nav.navbar_icon_txt=request.form['navbar_icon_txt']
      nav.navbar_icon_url =request.form['navbar_icon_url']
      db.session.commit()
      return redirect('/admin/navbar')
    return  loginCheck( render_template ('admin/navbarupdate.html',nav=nav))

# eminino1@gmail.com
# +994773523123
# end

# NavbarIcon
@app.route('/admin/navbaricon', methods=['GET','POST']) 
def navbaricon():
   icons=NavbarIcon.query.all()
   if request.method=='POST':
      icon=NavbarIcon(
      nav_icon_name=request.form['nav_icon_name'],
      nav_icon=request.form['nav_icon'],
      nav_icon_url=request.form['nav_icon_url']
      )     
      db.session.add(icon)
      db.session.commit()
      return redirect('/admin/navbaricon')
   return  loginCheck( render_template('admin/navbaricon.html',icons=icons))
   
   # update
@app.route("/admin/navbariconupdate/<id>" , methods=['GET','POST'])  
def navbariconupdate(id):
   icon=NavbarIcon.query.get(id)
   if request.method=='POST':
      icon.nav_icon_name=request.form['nav_icon_name']
      icon.nav_icon=request.form['nav_icon']
      icon.nav_icon_url=request.form['nav_icon_url']

      db.session.commit()
      return redirect('/admin/navbaricon')
   return loginCheck (render_template('admin/navbariconupdate.html',icon=icon))

@app.route("/admin/navbaricondelete/<id>")
def navbaricondelete(id):
   icon=NavbarIcon.query.get(id)
   db.session.delete(icon)
   db.session.commit()
   return redirect('/admin/navbaricon')

# navbar MENU
@app.route('/admin/navbarmenu', methods=['GET','POST']) 
def navbarmenu():
   menus=NavbarMenu.query.all()
   if request.method=='POST':
      menu=NavbarMenu(
      navbar_menu_name=request.form['navbar_menu_name'],
      navbar_menu_name_url=request.form['navbar_menu_name_url']
      )     
      db.session.add(menu)
      db.session.commit()
      return redirect('/admin/navbarmenu')
   return  loginCheck(render_template('admin/navbarmenu.html',menus=menus))
   
   # update
@app.route("/admin/navbarmenuupdate/<id>" , methods=['GET','POST'])  
def navbarmenuupdate(id):
   menu=NavbarMenu.query.get(id)
   if request.method=='POST':
      menu.navbar_menu_name=request.form['navbar_menu_name']
      menu.navbar_menu_name_url=request.form['navbar_menu_name_url']
      db.session.commit()
      return redirect('/admin/navbarmenu')
   return loginCheck( render_template('admin/navbarmenuupdate.html',menu=menu))

@app.route("/admin/navbarmenudelete/<id>")
def navbarmenudelete(id):
   menu=NavbarMenu.query.get(id)
   db.session.delete(menu)
   db.session.commit()
   return redirect('/admin/navbarmenu')


# end


# Navbar Slider

@app.route('/admin/slider', methods=['GET','POST']) 
def slider():
   sliders=NavbarSlider.query.all()
   if request.method=='POST':
      file=request.files['slider_img']
      filename=file.filename
      file.save(os.path.join (app.config['UPLOAD_FOLDER'],filename))
      slider=NavbarSlider(
       slider_img=filename,
        slider_heading=request.form['slider_heading'],
        slider_desc=request.form['slider_desc'],
        slider_btn_name=request.form['slider_btn_name']
      )     
      db.session.add(slider)
      db.session.commit()
      return redirect('/admin/slider')
   return loginCheck(render_template('admin/slider.html',sliders=sliders))

# delete
@app.route("/admin/sliderdelete/<id>")
def sliderdelete(id):
   slider=NavbarSlider.query.get(id)
   db.session.delete(slider)
   db.session.commit()
   return redirect('/admin/slider')


# update
@app.route("/admin/sliderupdate/<id>" , methods=['GET','POST']) 
def sliderupdate(id):
   slider=NavbarSlider.query.get(id)
   if request.method=='POST':
      file=request.files['slider_img']
      filename=file.filename
      file.save(os.path.join (app.config['UPLOAD_FOLDER'],filename))
      slider.slider_img=filename,
      slider.slider_heading=request.form['slider_heading'],
      sldier.slider_desc=request.form['slider_desc'],
      slider.slider_btn_name=request.form['slider_btn_name']
      db.session.commit()
      return redirect('/admin/slider')
   return loginCheck(render_template('admin/sliderupdate.html',slider=slider))

#  end



# About Heading
@app.route('/admin/aboutheading', methods=['GET','POST']) 
def adminAboutHeading():
   aboutheads=AboutHeading.query.all()
   if request.method=='POST':
      abouthead=AboutHeading(
         about_heading=request.form['about_heading'],
         about_desc=request.form['about_desc']
      )     
      db.session.add(abouthead)
      db.session.commit()
      return redirect('/admin/aboutheading')
   return loginCheck(render_template('admin/aboutheading.html',aboutheads=aboutheads))
   
@app.route("/admin/aboutheadingdelete/<id>")
def aboutheadingdelete(id):
   abouthead=AboutHeading.query.get(id)
   db.session.delete(abouthead)
   db.session.commit()
   return redirect('/admin/aboutheading')


@app.route("/admin/aboutheadingupdate/<id>" , methods=['GET','POST'])  
def aboutheadingupdate(id):
   abouthead=AboutHeading.query.get(id)
   if request.method=='POST':
      abouthead.about_heading=request.form['about_heading']
      abouthead.about_desc=request.form['about_desc']
      db.session.commit()
      return redirect('/admin/aboutheading')
   return loginCheck(render_template('admin/aboutheadingupdate.html',abouthead=abouthead))

# end



# about img
@app.route('/admin/aboutimg', methods=['GET','POST']) 
def aboutimg():
   posts=AboutImg.query.all()
   if request.method=='POST':
      file=request.files['about_img']
      filename=file.filename
      file.save(os.path.join (app.config['UPLOAD_FOLDER'],filename))
      post=AboutImg(
       about_img=filename

      )     
      db.session.add(post)
      db.session.commit()
      return redirect('/admin/aboutimg')
   return loginCheck (render_template('admin/aboutimg.html',posts=posts))

# delete
@app.route("/admin/aboutimgdelete/<id>")
def Aboutimgdelete(id):
   post=AboutImg.query.get(id)
   db.session.delete(post)
   db.session.commit()
   return redirect('/admin/aboutimg')


# update
@app.route("/admin/aboutimgupdate/<id>" , methods=['GET','POST']) 
def Aboutimgupdate(id):
   post=AboutImg.query.get(id)
   if request.method=='POST':
      file=request.files['about_img']
      filename=file.filename
      file.save(os.path.join (app.config['UPLOAD_FOLDER'],filename))
      post.about_img=filename
      db.session.commit()
      return redirect('/admin/aboutimg')
   return loginCheck (render_template('admin/aboutimgupdate.html',post=post))

#  end



# About
@app.route('/admin/aboutext', methods=['GET','POST']) 
def aboutext():
   aboutexts=About.query.all()
   if request.method=='POST':
      aboutext=About(
         about_subheading=request.form['about_subheading'],
         about_title=request.form['about_title']
      )     
      db.session.add(aboutext)
      db.session.commit()
      return redirect('/admin/aboutext')
   return loginCheck (render_template('admin/aboutext.html',aboutexts=aboutexts))
   
@app.route("/admin/aboutextdelete/<id>")
def aboutextdelete(id):
   aboutext=About.query.get(id)
   db.session.delete(aboutext)
   db.session.commit()
   return redirect('/admin/aboutext')


@app.route("/admin/aboutextupdate/<id>" , methods=['GET','POST'])  
def aboutextupdate(id):
   aboutext=About.query.get(id)
   if request.method=='POST':
      aboutext.about_subheading=request.form['about_subheading']
      aboutext.about_title=request.form['about_title']
      db.session.commit()
      return redirect('/admin/aboutext')
   return loginCheck (render_template('admin/aboutextupdate.html',aboutext=aboutext))

# 
# About list
@app.route('/admin/aboutlist', methods=['GET','POST']) 
def aboutlist():
   lists=AboutList.query.all()
   if request.method=='POST':
      list=AboutList(
      about_list_desc =request.form['about_list_desc']
    
      )     
      db.session.add(list)
      db.session.commit()
      return redirect('/admin/aboutlist')
   return loginCheck (render_template('admin/aboutlist.html',lists=lists))
   
   # update
@app.route("/admin/aboutlistupdate/<id>" , methods=['GET','POST'])  
def aboutlistupdate(id):
   list=AboutList.query.get(id)
   if request.method=='POST':
      list.about_list_desc=request.form['about_list_desc']
      db.session.commit()
      return redirect('/admin/aboutlist')
   return loginCheck (render_template('admin/aboutlistupdate.html',list=list))

@app.route("/admin/aboutlistdelete/<id>")
def aboutlistdelete(id):
   list=AboutList.query.get(id)
   db.session.delete(list)
   db.session.commit()
   return redirect('/admin/aboutlist')

# 

# AboutEnd
@app.route('/admin/aboutend', methods=['GET','POST']) 
def aboutend():
   txts=AboutEnd.query.all()
   if request.method=='POST':
      txt=AboutEnd(
       about_end_desc=request.form['about_end_desc']
    
      )     
      db.session.add(txt)
      db.session.commit()
      return redirect('/admin/aboutend')
   return loginCheck (render_template('admin/aboutend.html',txts=txts))
   
   # update
@app.route("/admin/aboutendupdate/<id>" , methods=['GET','POST'])  
def aboutendupdate(id):
   txt=AboutEnd.query.get(id)
   if request.method=='POST':
      txt.about_end_desc=request.form['about_end_desc']
      db.session.commit()
      return redirect('/admin/aboutend')
   return loginCheck (render_template('admin/aboutendupdate.html',txt=txt))

@app.route("/admin/aboutenddelete/<id>")
def aboutenddelete(id):
   txt=AboutEnd.query.get(id)
   db.session.delete(txt)
   db.session.commit()
   return redirect('/admin/aboutend')

# 

# Testimional
@app.route('/admin/testi', methods=['GET','POST']) 
def testi():
   numbers=Testimional.query.all()
   if request.method=='POST':
      number=Testimional(
      testi_number=request.form['testi_number'],
      testi_heading=request.form['testi_heading'],
      testi_title=request.form['testi_title']

      )     
      db.session.add(number)
      db.session.commit()
      return redirect('/admin/testi')
   return loginCheck (render_template('admin/testi.html',numbers=numbers))
   
   # update
@app.route("/admin/testiupdate/<id>" , methods=['GET','POST'])  
def testiupdate(id):
   number=Testimional.query.get(id)
   if request.method=='POST':
      number.testi_number=request.form['testi_number']
      number.testi_heading=request.form['testi_heading']
      number.testi_title=request.form['testi_title']

      db.session.commit()
      return redirect('/admin/testi')
   return loginCheck (render_template('admin/testiupdate.html',number=number))

@app.route("/admin/testidelete/<id>")
def testidelete(id):
   number=Testimional.query.get(id)
   db.session.delete(number)
   db.session.commit()
   return redirect('/admin/testi')

# 

# ClientHeading
@app.route('/admin/clientheading', methods=['GET','POST']) 
def clientheading():
   clientheads=ClientHeading.query.all()
   if request.method=='POST':
      clienthead=ClientHeading(
       client_heading=request.form['client_heading'],
       client_desc=request.form['client_desc']
      )     
      db.session.add(clienthead)
      db.session.commit()
      return redirect('/admin/clientheading')
   return loginCheck (render_template('admin/clientheading.html',clientheads=clientheads))
   
   # update
@app.route("/admin/clientheadingupdate/<id>" , methods=['GET','POST'])  
def clientheadingupdate(id):
   clienthead=ClientHeading.query.get(id)
   if request.method=='POST':
      clienthead.client_heading=request.form['client_heading']
      clienthead.client_desc=request.form['client_desc']
      db.session.commit()
      return redirect('/admin/clientheading')
   return  loginCheck (render_template('admin/clientheadingupdate.html',clienthead=clienthead))

@app.route("/admin/clientheadingdelete/<id>")
def clientheadingdelete(id):
   clienthead=ClientHeading.query.get(id)
   db.session.delete(clienthead)
   db.session.commit()
   return redirect('/admin/clientheading')
# 




# ClientImg
@app.route('/admin/client', methods=['GET','POST']) 
def client():
   logos=ClientImg.query.all()
   if request.method=='POST':
      file=request.files['logo_img']
      filename=file.filename
      file.save(os.path.join (app.config['UPLOAD_FOLDER'],filename))
      logo=ClientImg(
       logo_img=filename

      )     
      db.session.add(logo)
      db.session.commit()
      return redirect('/admin/client')
   return loginCheck(render_template('admin/client.html',logos=logos))

# delete
@app.route("/admin/clientdelete/<id>")
def clientdelete(id):
   logo=ClientImg.query.get(id)
   db.session.delete(logo)
   db.session.commit()
   return redirect('/admin/client')


# update
@app.route("/admin/clientupdate/<id>" , methods=['GET','POST']) 
def clientupdate(id):
   logo=ClientImg.query.get(id)
   if request.method=='POST':
      file=request.files['logo_img']
      filename=file.filename
      file.save(os.path.join (app.config['UPLOAD_FOLDER'],filename))
      logo.logo_img=filename
      db.session.commit()
      return redirect('/admin/client')
   return loginCheck (render_template('admin/clientupdate.html',logo=logo))

#  end

# 

# ServivesHeading
@app.route('/admin/serviceshead', methods=['GET','POST']) 
def bloghead():
   servicesheads=ServivesHeading.query.all()
   if request.method=='POST':
      serviceshead=ServivesHeading(
       services_heading=request.form['services_heading'],
       services_desc=request.form['services_desc']
      )     
      db.session.add(serviceshead)
      db.session.commit()
      return redirect('/admin/serviceshead')
   return loginCheck (render_template('admin/serviceshead.html',servicesheads=servicesheads))
   
   # update
@app.route("/admin/servicesheadupdate/<id>" , methods=['GET','POST'])  
def servicesheadupdate(id):
   serviceshead=ServivesHeading.query.get(id)
   if request.method=='POST':
      serviceshead.services_heading=request.form['services_heading']
      serviceshead.services_desc=request.form['services_desc']
      db.session.commit()
      return redirect('/admin/serviceshead')
   return loginCheck( render_template('admin/servicesheadupdate.html',serviceshead=serviceshead))

@app.route("/admin/servicesheaddelete/<id>")
def servicesheaddelete(id):
   serviceshead=ServivesHeading.query.get(id)
   db.session.delete(serviceshead)
   db.session.commit()
   return redirect('/admin/serviceshead')
# 


# Servives
@app.route('/admin/service', methods=['GET','POST']) 
def service():
   blogs=Servives.query.all()
   if request.method=='POST':
      blog=Servives(
      service_icon_name=request.form['service_icon_name'],
      service_subheading_url=request.form['service_subheading_url'],
      service_icon=request.form['service_icon'],
      service_subheading=request.form['service_subheading'],
      service_text=request.form['service_text']
   
      )     
      db.session.add(blog)
      db.session.commit()
      return redirect('/admin/service')
   return loginCheck( render_template('admin/service.html',blogs=blogs))
   
@app.route("/admin/servicedelete/<id>")
def servicesdelete(id):
   blog=Servives.query.get(id)
   db.session.delete(blog)
   db.session.commit()
   return redirect('/admin/service')


@app.route("/admin/serviceupdate/<id>" , methods=['GET','POST'])  
def serviceupdate(id):
   blog=Servives.query.get(id)
   if request.method=='POST':
      blog.service_icon_name=request.form['service_icon_name']
      blog.service_icon=request.form['service_icon']
      blog.service_subheading_url=request.form['service_subheading_url']
      blog.service_subheading=request.form['service_subheading']
      blog.service_text=request.form['service_text']
    
      db.session.commit()
      return redirect('/admin/service')
   return loginCheck(render_template('admin/serviceupdate.html',blog=blog))


# 


#  PortHeading
@app.route('/admin/port', methods=['GET','POST']) 
def port():
   ports=PortHeading.query.all()
   if request.method=='POST':
      port=PortHeading(
       port_heading=request.form['port_heading'],
       port_desc=request.form['port_desc']
      )     
      db.session.add(port)
      db.session.commit()
      return redirect('/admin/port')
   return render_template('admin/port.html',ports=ports)
   
   # update
@app.route("/admin/portupdate/<id>" , methods=['GET','POST'])  
def portupdate(id):
   port=PortHeading.query.get(id)
   if request.method=='POST':
      port.port_heading=request.form['port_heading']
      port.port_desc=request.form['port_desc']
      db.session.commit()
      return redirect('/admin/port')
   return loginCheck(render_template('admin/portupdate.html',port=port))

@app.route("/admin/portdelete/<id>")
def portdelete(id):
   port=PortHeading.query.get(id)
   db.session.delete(port)
   db.session.commit()
   return redirect('/admin/port')


# 

# Portfolio
@app.route('/admin/portfolio', methods=['GET','POST']) 
def portfolio():
   links=Portfolio.query.all()
   if request.method=='POST':
      file=request.files['portfolio_img']
      filename=file.filename
      file.save(os.path.join (app.config['UPLOAD_FOLDER'],filename))
      link=Portfolio(
         portfolio_img_link=request.form['portfolio_img_link'],
         portfolio_img_head=request.form['portfolio_img_head'],
         portfolio_img_desc=request.form['portfolio_img_desc'],
         portfolio_img=filename

      )     
      db.session.add(link)
      db.session.commit()
      return redirect('/admin/portfolio')
   return loginCheck( render_template('admin/portfolio.html',links=links))

# delete
@app.route("/admin/portfoliodelete/<id>")
def porfoliodelete(id):
   link=Portfolio.query.get(id)
   db.session.delete(link)
   db.session.commit()
   return redirect('/admin/portfolio')


# update
@app.route("/admin/portfolioupdate/<id>" , methods=['GET','POST']) 
def portfolioupdate(id):
   link=Portfolio.query.get(id)
   if request.method=='POST':
      file=request.files['portfolio_img']
      filename=file.filename
      file.save(os.path.join (app.config['UPLOAD_FOLDER'],filename))
      link.portfolio_img_link=request.form['portfolio_img_link']
      link.portfolio_img_head=request.form['portfolio_img_head']
      link.portfolio_img_desc=request.form['portfolio_img_desc']
      link.portfolio_img=filename
      db.session.commit()
      return redirect('/admin/portfolio')
   return loginCheck (render_template('admin/portfolioupdate.html',link=link))

# 



# ContactHeading
@app.route('/admin/contactheading', methods=['GET','POST']) 
def contactheading():
   contacts=ContactHeading.query.all()
   if request.method=='POST':
      contact=ContactHeading(
      contact_heading =request.form['contact_heading'],
      contact_desc=request.form['contact_desc']
      )     
      db.session.add(contact)
      db.session.commit()
      return redirect('/admin/contactheading')
   return loginCheck (render_template('admin/contactheading.html',contacts=contacts))
   
   # update
@app.route("/admin/contactheadingupdate/<id>" , methods=['GET','POST'])  
def contactupdate(id):
   contact=ContactHeading.query.get(id)
   if request.method=='POST':
      contact.contact_heading=request.form['contact_heading']
      contact.contact_desc=request.form['contact_desc']
      db.session.commit()
      return redirect('/admin/contactheading')
   return loginCheck( render_template('admin/contactheadingupdate.html',contact=contact))

@app.route("/admin/contactheadingdelete/<id>")
def contactdelete(id):
   contact=ContactHeading.query.get(id)
   db.session.delete(contact)
   db.session.commit()
   return redirect('/admin/contactheading')

# 


# ContactMe

@app.route('/admin/icon', methods=['GET','POST']) 
def icon():
   endicons=ContactMe.query.all()
   if request.method=='POST':
      endicon=ContactMe(
      ct_icon_name=request.form['ct_icon_name'],
      ct_icon=request.form['ct_icon'],
      ct_heading=request.form['ct_heading'],
      ct_desc=request.form['ct_desc'],
      ct_link=request.form['ct_link']
    
      )     
      db.session.add(endicon)
      db.session.commit()
      return redirect('/admin/icon')
   return loginCheck(render_template('admin/icon.html',endicons=endicons))
   
   # update
@app.route("/admin/iconupdate/<id>" , methods=['GET','POST'])  
def iconupdate(id):
   endicon=ContactMe.query.get(id)
   if request.method=='POST':
      endicon.ct_icon_name=request.form['ct_icon_name']
      endicon.ct_icon=request.form['ct_icon']
      endicon.ct_heading=request.form['ct_heading']
      endicon.ct_desc=request.form['ct_desc']
      endicon.ct_link=request.form['ct_link']

      db.session.commit()
      return redirect('/admin/icon')
   return loginCheck( render_template('admin/iconupdate.html',endicon=endicon))

@app.route("/admin/icondelete/<id>")
def icondelete(id):
   endicon=ContactMe.query.get(id)
   db.session.delete(endicon)
   db.session.commit()
   return redirect('/admin/icon')
# 


# SocialIcon
@app.route('/admin/social', methods=['GET','POST']) 
def social():
   socials=SocialIcon.query.all()
   if request.method=='POST':
      social=SocialIcon(
      social_icon_name=request.form['social_icon_name'],
      social_icon=request.form['social_icon'],
      social_icon_link=request.form['social_icon_link']
      )     
      db.session.add(social)
      db.session.commit()
      return redirect('/admin/social')
   return loginCheck( render_template('admin/social.html',socials=socials))
   
   # update
@app.route("/admin/socialupdate/<id>" , methods=['GET','POST'])  
def socialupdate(id):
   social=SocialIcon.query.get(id)
   if request.method=='POST':
      social.social_icon_name=request.form['social_icon_name']
      social.social_icon=request.form['social_icon']
      social.social_icon_link=request.form['social_icon_link']

      db.session.commit()
      return redirect('/admin/social')
   return loginCheck (render_template('admin/socialupdate.html',social=social))

@app.route("/admin/socialdelete/<id>")
def socialdelete(id):
   social=SocialIcon.query.get(id)
   db.session.delete(social)
   db.session.commit()
   return redirect('/admin/social')




# 