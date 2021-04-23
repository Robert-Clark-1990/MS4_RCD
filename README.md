# Milestone Project 4 - Robert Clark Design

- [Host Link](https://robertclarkdesign.herokuapp.com/)
- [GitHub Repo Link](https://github.com/Robert-Clark-1990/MS4_RCD)

# Table of Contents

 - [**Introduction**](#introduction)

 - [**User Experience**](#user-experience)
    - [Project Goals](#project-goals)
    - [User Stories](#user-stories)
    - [Wireframes](#wireframes)
    - [Site Design](#site-design)
    - [Database Design](#database-design)

 - [**Features**](#features)
    - [Existing Features](#existing-features)
    - [Future Features To implement](#future-features-to-implement)

 - [**Technologies Used**](#technologies-used)
    - [Languages](#languages)
    - [APIS and Frameworks](#apis-and-frameworks)
    - [Hosting Databases and Version Control](#hosting-databases-and-version-control)
    - [Websites](#websites)

 - [**Testing**](#testing)
    - [Bug Fixes](#bug-fixes)
    - [Browser Compatibility](#browser-compatibility)
    - [Responsive Design](#responsive-design)
    - [Validator Tests](#validator-tests)
    - [Meeting Project Needs](#meeting-project-needs)

 - [**Deployment**](#deployment)
    - [Heroku Deployment](#heroku-deployment)
    - [Running This Project Locally](#running-this-project-locally)

 - [**Credits**](#credits)
    - [Content](#content)
    - [Media](#media)
    - [Code](#code)
    - [Acknowledgements](#acknowledgements)

---

# Introduction

`<-- INSERT SITE IMAGE -->`

For the final project in the Code Institute course, I wanted to create something personal and important to me and my future as a Software Developer. I have been a hugely creative individual
my whole life, and have worked in the past as a freelance Graphic Designer and Digital Marketer through the moniker of **Robert Clark Design**. I decided that I wanted to build this final project 
into a portfolio of my work and a place where I can sell my design and development services.

---

# User Experience

## Project Goals

**Robert Clark Design** is a full stack website that showcases a portfolio of design and development projects. The purpose is to demonstrate the work and skillset of the site user in an inviting and stylish way in order to encourage site visitors to request and purchase an array of available products, or purchase a commission package. Once a user has purchased a product, they will be able to log in via the email and password and view their order history, or if they purchased a commission package, they will be able to upload images for reference, and view the status of their work. The site owner will be able to upload the finished product via the website, which the customer will then be able to either accept or request a round of changes. Once the customer has accepted, they will be invited to leave a testimonial which will display on the site.


## User Stories

| ID  |   As A       |  I want to be able to...                                                                        |
| --- | :----------  | :---------------------------------------------------------------------------------------------- |
| 01  | Site User    | Quickly and easily understand the purpose of the site                                           |
| 02  | Site User    | View a list of products & services available                                                    |
| 03  | Site User    | View individual products & services                                                             |
| 04  | Site User    | Sort for products & services that fit my requirements                                           |
| 05  | Site User    | Select products & services I want and add them to my basket                                     |
| 06  | Site User    | Easily view the total cost of my purchases at any time                                          |
| 07  | Site User    | Order prepackaged services such as commissioned artwork and receive an automated quote          |
| 08  | Site User    | Add additional information to inform designer on project requirements                           |
| 09  | Site User    | Easily locate an inbuilt contact form to request quotes on unique projects                      |
| 10  | Site User    | Pay for services via an inbuilt payment service                                                 |
| 11  | Site User    | Sign in as a customer to view status of project                                                 |
| 12  | Site User    | View the completed work, accept the result or request a round of changes                        |
| 13  | Site User    | Download completed work and share it on Social Media                                            |
| 14  | Site Owner   | Log in as a special user and view a list of all orders                                          |
| 15  | Site Owner   | Handle the customer request and upload of completed work all through the site                   |
| 16  | Site Owner   | Showcase a portfolio of work which can be changed or removed through the site                   |
| 17  | Site Owner   | Showcase testimonials from previous customers which can be removed through the site             |
| 18  | Site Owner   | Display an about the designer section to humanise the work and encourage users to commit        |
| 19  | Site Owner   | Invite customers to write a testimonial upon project completion and have it display on the site |
| 20  | Site Owner   | Add, edit, view and delete items in the shop all through the site                               |


## Wireframes

In order to visualise the project before creation, a series of wireframes were created. These outlined the basic structure of the site and the individual page layouts. Over the course of
the project, the designs evolved to meet the expanded scope, however the basic structure and design remained intact. 

`<-- INSERT WIREFRAME IMAGES AND PDF LINK -->`


## Site Design

In order to draw focus to the work in the portfolio, the site will have a clean, minimalist design, encouraging white space where possible. This will be juxtaposed through the use of geometric art, which is favoured by the site owner and used throughout his work.

### Colour Scheme

In keeping with the site logo, vibrant primary colours will be used alongside a white background to draw attention to the work. However, the site will not be limited to the use of primary colours and will expand where necessary to encourage site users to view everything the site has to offer.

### Typography

To match the minimalistic design of the site, the Google Font [Poppins](https://fonts.google.com/specimen/Poppins?preview.text=Robert%20Clark%20Design&preview.text_type=custom) was used. This font was selected to ensure user accessibility and readibility was always at the forefront of site design.

### Artwork

A strong focus on geometric design was used throughout the site, showcasing the site owner's penchant for the style. However, this was never limited to solely this style as the main purpose of the site was to showcase a wide array of talent. This is never more prevalent than on the portfolio page, wherein the site user can view a range of the site owner's previous work.


## Database Design

All data related to this project is saved in JSON files across three apps. The Portfolio app is separated from the rest as it contains data from previous works, and would only be updated with new information if a new client was taken on. The Products app contains JSON files for Products and Categories. Users who purchase a commission package will then be invited to leave a testimonial, which will bring forward data to be used in the Testimonials app.
The model below was created using [Draw SQL](https://drawsql.app/rob-clark/diagrams/rcd)

![Database Schema](documents/images/database-schema.png)

---

# Features

## Existing Features

To realise the goals of the project, the following features were implemented:

`<-- TO FINISH -->`

### Home Page 

### About Page

### Portfolio Page

### Individual Project Page

### Testimonials Page

### Store Page

### Shopping Bag Page

### Checkout Page

### Log In Page

### Customer Project Page

### Contact Page

A contact page was added [with thanks to LearnDjango.com](https://learndjango.com/tutorials/django-email-contact-form) to allow site users who wish to enquire about the site owner's services a quick and simple way of communication. At present, these emails post to the terminal, however this will be fixed to send emails properly when the site goes live, using a service such as [SendGrid](https://sendgrid.com/), [mailgun](https://www.mailgun.com/) or [Amazon's SES](https://aws.amazon.com/ses/) to complete the process.


## Future Features To Implement

* The implementation of an inbuilt chat feature would add an extra layer of communication between site user and site owner. Users would be able to check in on the status of their project, and
request minor changes easily.

* Site users can sign in and create an account using their social media accounts such as Facebook or Instagram. This would allow a more seemless integration for users to register an account and
share work upon completion.

---

# Technologies Used

`<-- TO FINISH -->`

## Languages

* [HTML5](https://en.wikipedia.org/wiki/HTML5)

   HTML5 was used to provide the structure and content of this project.

* [CSS3](https://en.wikipedia.org/wiki/CSS)

   CSS3 was used to style to the HTML5 elements.

* [JQuery](https://jquery.com/)

   JQuery was used to provide JavaScript functionality.

* [Python](https://www.python.org/)

   Python was used to provide the backend of this project.


## APIS and Frameworks

## Hosting Databases and Version Control

* [MongoDB](https://www.mongodb.com/)

   MongoDB was used to store the database used in this project.

* [Git](https://git-scm.com/)

   Git was used for version control, utilising the Gitpod terminal to commit to Git and Push to GitHub.

* [GitHub](https://github.com/)

   GitHub was used to store the project.
   
* [Heroku](https://www.heroku.com/)

   Heroku was used to deploy this site.

## Websites

* [Google Fonts](https://fonts.google.com/specimen/Poppins?preview.text=Robert%20Clark%20Design&preview.text_type=custom)

   The Poppins Google Font was used as the primary font in this project.

* [TinyPNG](https://tinypng.com/)

   Tinypng was used to optimise jpg and png images to increase performance.

* [W3C Markup Validation](https://validator.w3.org/#validate_by_input) 

   W3C Markup Validation was used to ensure HTML met the necessary standards.

* [Jigsaw](https://jigsaw.w3.org/css-validator/) 

   Jigsaw was used to validate CSS code used in the project.

* [JS Hint](https://jshint.com/) 
   
   JS Hint was used to validate JavaScript code used in the project.

* [PEP8](http://pep8online.com/) 

   PEP8 was used to validated Python code used in this project.


---

# Testing

## Bug Fixes

- **Adjust Quantity Buttons** - During development of the bag app, an issue arose in which the plus and minus buttons to adjust quantity of an item in the bag didn't function properly. The script was implemented on the product_detail page, wherein it worked perfectly fine, but the same could not be said for the bag page. As this was copied from the product_detail page, which in turn was near verbatim from the Boutique Ado walkthrough project, the code was studied and compared to that in the walkthrough. However there were no differences - aside from the exclusion of the sizing if else statement as no sizes were required on this project.
The fix came when the copied code from the product_detail page was deleted entirely, then rewritten manually from scratch. Though it was identical, to how it had been before, the code now worked.

- **Checkout Webhook** -
During the creation of webhooks to ensure the Stripe payments would work as intended, a 500 error was being raised when a payment was submitted. Both the payment_intent.created and charge.succeeded went go through as intended, but the payment_intent.succeeded did not without manually resubmitting it in the Stripe dashboard. The terminal raised a ValueError saying the view checkout.webhooks.webhook didn’t return a HttpResponse object, and returned None instead. 
The issue came from the webhooks_handler.py file, which was missing a return at the end of the handle_payment_intent_succeeded function's else statement. Once this was included, the error was resolved.

- **Duplicate Street_address1** -
During tests of the payment system, an error appeared to show that the street_address2 input was being overridden by a second street_address1. On closer inspection, this turned out to be a simple error on the checkout_success.html page wherein the street_address1 tag had been repeated and not changed to street_address2.

- **Unresponsible CSS/JS files** -
During production, an error arose in which any CSS or JS files outside the base files were not working as intended. Research underway to see if this was an issue with Bootstrap or Django, but in the end the answer was much simpler. In the base.html file, the extra_css and extra_js blocks had been written as extracss and extrajs, meaning they weren't picking up new block files. This fix in turn solved all outstanding CSS and JS issues.

- **NoReverseMatch** -
During the creation of add/edit functions on the Portfolio and Testimonials, an error arose wherein a NoReverseMatch error was raising when attempting to reach the edit pages. After further research, this was an issue that arose from the project.id missing from the {% url 'edit_project' %} links.
 
 - **SECRET_KEY** -
 Once the project had been deployed to Heroku and the Static and Media files were stored on AWS, two issues arose the next time the project was opened on Gitpod. The first was this warning:
 `django.core.exceptions.ImproperlyConfigured: The SECRET_KEY setting must not be empty.`
 This came as a surprise as there had been no issues with the SECRET_KEY thus far, and the deployed Heroku version worked fine. To fix this, a env.py file was created to store the SECRET_KEY, and - surprisingly - the following was added to the settings.py file: `SECRET_KEY = os.environ.get('SECRET_KEY', 'some value if your key is not in the environment') `
 The error no longer appeared, and since it appears to be a Gitpod-side problem, there should be no forseeable issues in the future of the project.

 - **Media and Static Files Not Loading**
The second of the two post-deployment issues, when the Gitpod server was run all the media and static files no longer loaded after the Heroku deployment. At first, this was thought to be an issue with the `DISABLE_COLLECTSTATIC`, but this was not the case. Instead, it appeared to be a fault with the site attempting to load local files instead of the hosted AWS files. This was not the case on the Heroku site, so to fix the `USE_AWS` variable was added to the Gitpod environment. This solved the issue, however care was needed to ensure any changes made on local css files were pushed to AWS.

## Bugs Unable To Fix

- **Product Page Pagination** -
During the later stages of development, it was suggested pagination was implemented into the products page. This was done using the Paginator import in the products view. However, once implemented, this first threw up **UnorderedObjectListWarning: Pagination may yeild inconsistent results with an unordered object_list**. To counter this, the products object was set to order by the pk value, which stopped the error from appearing. However a bigger issue arose in that the page would no longer view properly, and would show raw code instead. Upon inspection it appeared the whole page had been placed in a "pre" block, which showed no errors in the terminal, or Chrome's DevTools. As this was a complementary feature implemented late into the project, it was decided that it would be removed for the time being. The code from the products views.py file can be viewed below:

```
from django.core.paginator import Paginator

def all_products(request):

    products = Product.objects.order_by('-pk').all()
    categories = None
    paginator = Paginator(products, 12)

    if request.GET:
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'products': products,
        'current_categories': categories,
    }

    return render(request, 'products/products.html', {'page_obj': page_obj}, context) 
```


## Browser Compatibility

## Responsive Design

## Validator Tests

### W3 HTML Validator 

### Jigsaw CSS Validator

### JSHint JS Validator

### PEP8 Python Validator 

## Meeting Project Needs

---

# Deployment

## Heroku Deployment

## Running This Project Locally

---

# Credits

### Content

- Written content, portfolio work, and other designs showcased were created by the developer, [Robert Clark](https://github.com/Robert-Clark-1990).

### Media

- All media and designs created by the developer, [Robert Clark](https://github.com/Robert-Clark-1990).

### Code

- Image Modal from [W3Schools](https://www.w3schools.com/css/tryit.asp?filename=trycss_image_modal_js)

- Arrow Up CSS from [CSS-Tricks](https://css-tricks.com/snippets/css/css-triangle/)

- Image Hover from [css-workshop](http://css-workshop.com/hover-box-text-over-images-on-hover-and-more/)

- Arrow Scroll Down CSS from [CSSHint](https://csshint.com/html-css-scroll-down-arrow-examples/)

- Vertical Timeline from [Sanchit Sharma](https://codepen.io/web_designer_sanchit/pen/eLjvyw)

- Animate Scroll Elements from [Dev Tips and Tricks](https://www.dev-tips-and-tricks.com/animate-elements-scrolled-view-vanilla-js)

- Contact Form from [LearnDjango.com](https://learndjango.com/tutorials/django-email-contact-form)

- Profile Accordion from [W3Schools](https://www.w3schools.com/howto/howto_js_accordion.asp)

- Image Upload functionality with help from [cgpalmer](https://github.com/cgpalmer/ms4/tree/master/profiles)

### Acknowledgements

- Thanks to **Precious Ijege** for his continued assistance as mentor.

- Thanks to the **Code Institute tutors** who were there in times of crisis to help guide this developer in the right direction.
