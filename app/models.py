from enum import unique
from app import db

class NavbarInfo(db.Model):
  id=db.Column(db.Integer,primary_key=True)
  navbar_icon_name=db.Column(db.String(50))
  navbar_icon=db.Column(db.String(50))
  navbar_icon_txt=db.Column(db.String(50))
  navbar_icon_url=db.Column(db.String(50))

class NavbarIcon(db.Model):
  id=db.Column(db.Integer,primary_key=True)
  nav_icon_name=db.Column(db.String(50))
  nav_icon=db.Column(db.String(50))
  nav_icon_url=db.Column(db.String(50))


class NavbarMenu(db.Model):
 id=db.Column(db.Integer,primary_key=True)
 navbar_menu_name=db.Column(db.String(50))
 navbar_menu_name_url=db.Column(db.String(50))


class NavbarSlider(db.Model):
 id=db.Column(db.Integer,primary_key=True)
 slider_img=db.Column(db.String(50))
 slider_heading=db.Column(db.String(50))
 slider_desc=db.Column(db.String(50))
 slider_btn_name=db.Column(db.String(50))


class AboutHeading(db.Model):
 id=db.Column(db.Integer,primary_key=True)
 about_heading=db.Column(db.String(50))
 about_desc=db.Column(db.String(50))


class AboutImg(db.Model):
 id=db.Column(db.Integer,primary_key=True)
 about_img=db.Column(db.String(50))

class About(db.Model):
 id=db.Column(db.Integer,primary_key=True)
 about_subheading=db.Column(db.String(50))  
 about_title=db.Column(db.String(50))  



class AboutList(db.Model):
  id=db.Column(db.Integer,primary_key=True)
  about_list_desc=db.Column(db.String(50)) 
 
class AboutEnd(db.Model):
 id=db.Column(db.Integer,primary_key=True)
 about_end_desc=db.Column(db.String(50)) 

class Testimional(db.Model):
 id=db.Column(db.Integer,primary_key=True)
 testi_number=db.Column(db.String(50)) 
 testi_heading=db.Column(db.String(50)) 
 testi_title=db.Column(db.String(50)) 


class ClientHeading(db.Model):
 id=db.Column(db.Integer,primary_key=True)
 client_heading=db.Column(db.String(50)) 
 client_desc=db.Column(db.String(50))

class ClientImg(db.Model):
 id=db.Column(db.Integer,primary_key=True)
 logo_img=db.Column(db.String(50))


class ServivesHeading(db.Model):
 id=db.Column(db.Integer,primary_key=True)
 services_heading=db.Column(db.String(50)) 
 services_desc=db.Column(db.String(50))

class Servives(db.Model):
 id=db.Column(db.Integer,primary_key=True)
 service_icon_name=db.Column(db.String(50))
 service_icon=db.Column(db.String(50)) 
 service_subheading=db.Column(db.String(50))
 service_subheading_url=db.Column(db.String(50))
 service_text=db.Column(db.String(50))

class PortHeading(db.Model):
 id=db.Column(db.Integer,primary_key=True)
 port_heading=db.Column(db.String(50))
 port_desc=db.Column(db.String(50)) 

class Portfolio(db.Model):
 id=db.Column(db.Integer,primary_key=True)
 portfolio_img=db.Column(db.String(50))
 portfolio_img_head=db.Column(db.String(50)) 
 portfolio_img_desc=db.Column(db.String(50)) 
 portfolio_img_link=db.Column(db.String(50)) 

class ContactHeading(db.Model):
 id=db.Column(db.Integer,primary_key=True)
 contact_heading=db.Column(db.String(50))
 contact_desc=db.Column(db.String(50)) 

class ContactMe(db.Model):
 id=db.Column(db.Integer,primary_key=True)
 ct_icon_name=db.Column(db.String(50))
 ct_icon=db.Column(db.String(50))
 ct_heading=db.Column(db.String(50))
 ct_desc=db.Column(db.String(50)) 
 ct_link=db.Column(db.String(50)) 



class Contact(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    user_name=db.Column(db.String(50))
    user_email=db.Column(db.String(50))
    user_message=db.Column(db.Text)



class SocialIcon(db.Model):
 id=db.Column(db.Integer,primary_key=True)
 social_icon_name=db.Column(db.String(50))
 social_icon=db.Column(db.String(50)) 
 social_icon_link=db.Column(db.String(50)) 