from unicodedata import category
from django.db.models.fields import EmailField
from django.http import request
from django.shortcuts import render
from .models import add_category_table, add_user_table, reg_table, add_reservation_form,add_equipment_table,add_package_table,add_category_table,add_user_table,contact_form
from django.contrib import messages, auth

# Create your views here.
def index1(request):
    return render(request, "index1.html", )
def add_contact_form(request):
    if request.method == "POST":
        ex1 = contact_form(
            product_name=request.POST["product_name"],
            email=request.POST["email"],
            full_name=request.POST["full_name"],
            phone=request.POST["phone"],
            message=request.POST["message"],)

        ex1.save()
        print("saved")
        
        contact = contact_form.objects.all()
        return render(request, "index1.html", {"contact": contact})



def login(request):
    return render(request, "login.html")


def register(request):
    return render(request, "register.html")


def index(request):
    return render(request, "index.html")


def reg_form_submission(request):
    if request.method == "POST":
        if reg_table.objects.filter(
            email_id=request.POST["email_id"], contact_no=request.POST["contact_no"]
        ).exists():
            messages.error(
                request,
                "this email-id or contact number is already registered!...",
                extra_tags="email_contact",
            )
            return render(request, "register.html")
        elif reg_table.objects.filter(email_id=request.POST["email_id"]).exists():
            messages.error(
                request,
                "this email-id is already registered!...",
                extra_tags="email_contact",
            )
            return render(request, "register.html")
        elif reg_table.objects.filter(contact_no=request.POST["contact_no"]).exists():
            messages.error(
                request,
                "this contact number is already registered!...",
                extra_tags="email_contact",
            )
            return render(request, "register.html")
        else:
            ex1 = reg_table(
                username=request.POST["username"],
                email_id=request.POST["email_id"],
                password=request.POST["password"],
                con_password=request.POST["con_password"],
                contact_no=request.POST["contact_no"],
            )
            ex1.save()
            print("inside")
            messages.error(
                request,
                "your registration has completed successfully!..",
                extra_tags="reg_success",
            )
            return render(request, "login.html")
    else:
        print("outside")
        return render(request, "register.html")


def login_form_submission(request):
    if reg_table.objects.filter(
        email_id=request.POST["email_id"], password=request.POST["password"]
    ).exists():

        messages.error(request, "login successful!...", extra_tags="login_success")
        return render(request,"index.html")
    else:
        messages.error(request, "Invalid email or password", extra_tags="failed_login")
        return render(request, "login.html")


def logout(request):
    auth.logout(request)
    return render(request, "login.html")

#reservation page

def reservation(request):
    reservation = add_reservation_form.objects.all()
    return render(request, "reservation.html", {"reservation": reservation})
def add_new_reservation(request):
    return render(request, "add_new_reservation.html")
def add_reservation(request):
    if request.method == "POST":
        ex1 = add_reservation_form(
            unique_no=request.POST["unique_no"],
            item=request.POST["item"],
            datetime_From=request.POST["datetime_From"],
            datetime_To=request.POST["datetime_To"],
            status=request.POST["status"],)

        ex1.save()
        print("saved")
        messages.error(request,"your reservation has added successfully!..",extra_tags="reservation_success")
        reservation = add_reservation_form.objects.all()
        return render(request, "reservation.html", {"reservation": reservation})
    else:
        return render(request, "add_new_reservation.html")
def update_reservation(request, id):
    view_data = add_reservation_form.objects.get(id=id)
    return render(request, "update_reservation.html", {"view_data": view_data})
def update_reservation_form(request, id):
    if request.method == "POST":
        ex1 = add_reservation_form.objects.filter(id=id).update(
            unique_no=request.POST["unique_no"],
            item=request.POST["item"],
            datetime_From=request.POST["datetime_From"],
            datetime_To=request.POST["datetime_To"],
            status=request.POST["status"],)

        messages.error(request, "Successfully updated!...", extra_tags="reservation_success")
        reservation = add_reservation_form.objects.all()
        return render(request, "reservation.html", {"reservation": reservation})
    
def delete_reservation_list(request,id):
    view_data = add_reservation_form.objects.get(id=id)
    view_data.delete()
    print('delete')
    messages.error(request, "Successfully deleted!...", extra_tags="delete_success")
    reservation = add_reservation_form.objects.all()
    return render(request, "reservation.html", {"reservation": reservation})
def invoice(request):
    return render(request, "invoice.html")



# Equipment page

def equipments(request):
    equipments=add_equipment_table.objects.all()
    return render(request,"equipments.html",{"equipments":equipments})
def add_equipments(request):
    return render(request, "add_equipments.html")
def add_equipment_form(request):
    if request.method == "POST":
        ex1=add_equipment_table(eqp_name=request.POST["eqp_name"],
                            description=request.POST["description"],
                            category=request.POST["category"],
                            count=request.POST["count"])

        ex1.save()
        print("saved_equipment")
        messages.error(request,"your equipment has added successfully!..",extra_tags="eqp_success")
        equipments=add_equipment_table.objects.all()
        return render(request,"equipments.html",{"equipments":equipments})  
    else:
        return render(request, "add_equipments.html")

def edit_equipment(request, id):
    view_data = add_equipment_table.objects.get(id=id)
    return render(request, "upload_equipments.html", {"view_data": view_data})
def edit_equipment_form(request, id):
    if request.method == "POST":
        ex1 = add_equipment_table.objects.filter(id=id).update(
           eqp_name=request.POST['eqp_name'],
           description=request.POST['description'],
           category=request.POST['category'],
           count=request.POST['count'],)
           

        messages.error(request, "Successfully updated!...", extra_tags="reservation_success")
        equipments = add_equipment_table.objects.all()
        return render(request, "equipments.html", {"equipments": equipments})

def delete_equipment_list(request,id):
    view_data = add_equipment_table.objects.get(id=id)
    view_data.delete()
    print('delete eqp')
    messages.error(request, "Successfully deleted!...", extra_tags="delete_success")
    equipments=add_equipment_table.objects.all()
    return render(request,"equipments.html",{"equipments":equipments})

# Package page
def view_package(request):
    packages=add_package_table.objects.all()
    return render(request,"view_package.html",{"packages": packages})
def create_package(request):
    return render(request, "create_package.html")
def create_package_form(request):
     if request.method == "POST":
        ex1=add_package_table(package_name=request.POST["package_name"],
                            count=request.POST["count"],
                            status=request.POST["status"])
        ex1.save()
        messages.error(request,"your package has added successfully!..",extra_tags="package_success")
        packages=add_package_table.objects.all()
        return render(request,"view_package.html",{"packages": packages})
     else:
        return render(request, "create_package.html") 
def edit_package(request,id):
    view_data=add_package_table.objects.get(id=id)
    return render(request, "edit_package.html",{'view_data': view_data})
def edit_package_form(request, id):
    if request.method == "POST":
        ex1 = add_package_table.objects.filter(id=id).update(
            package_name=request.POST["package_name"],
            count=request.POST["count"],
            status=request.POST["status"],)

        messages.error(request, "Successfully updated!...", extra_tags="reservation_success")
        packages=add_package_table.objects.all()
        return render(request,"view_package.html",{"packages": packages})
def delete_package_list(request,id):
    view_data=add_package_table.objects.get(id=id)
    view_data.delete()
    messages.error(request,"your package deleted successfully!..",extra_tags="package_delete")
    packages=add_package_table.objects.all()
    return render(request,"view_package.html",{"packages": packages})

# Category page

def view_categories(request):
    category = add_category_table.objects.all()
    return render(request, "view_categories.html", {"category": category})
def add_categories(request):
    return render(request, "add_categories.html")
def add_category_form(request):
    if request.method == "POST":
        ex1 = add_category_table(
            product_name=request.POST["product_name"],
            product_id=request.POST["product_id"],
            status=request.POST["status"],)

        ex1.save()
        print("saved")
        messages.error(request,"your category has added successfully!..",extra_tags="reservation_success")
        category = add_category_table.objects.all()
        return render(request, "view_categories.html", {"category": category})
    else:
        return render(request, "add_new_reservation.html")
def edit_categories(request,id):
    view_data=add_category_table.objects.get(id=id)
    return render(request, "edit_categories.html",{'view_data': view_data})
def edit_category_form(request, id):
    if request.method == "POST":
        ex1 = add_category_table.objects.filter(id=id).update(
            product_name=request.POST["product_name"],
            product_id=request.POST["product_id"],
            status=request.POST["status"],)

        messages.error(request, "Successfully updated!...", extra_tags="reservation_success")
        category = add_category_table.objects.all()
        return render(request, "view_categories.html", {"category": category})
def delete_category_list(request,id):
    view_data = add_category_table.objects.get(id=id)
    view_data.delete()
    print('delete')
    messages.error(request, "Successfully deleted!...", extra_tags="delete_success")
    category = add_category_table.objects.all()
    return render(request, "view_categories.html", {"category": category})

# User page

def userlst(request):
    users = add_user_table.objects.all()
    return render(request, "userlst.html", {"users": users})
def add_user(request):
    return render(request, "add_user.html")
def add_user_form(request):
    if request.method == "POST":
        ex1 = add_user_table(
            user_name=request.POST['user_name'],
            email=request.POST['email'],
            registration=request.POST['registration'],
            designation=request.POST['designation'],
            status=request.POST['status'])

        ex1.save()
        print("saved")
        messages.error(request,"your user has added successfully!..",extra_tags="reservation_success")
        users = add_user_table.objects.all()
        return render(request, "userlst.html", {"users": users})
    else:
        return render(request, "add_user.html")
def edit_user(request,id):
    view_data=add_user_table.objects.get(id=id)
    return render(request, "edit_user.html",{'view_data': view_data})
def edit_user_form(request, id):
    if request.method == "POST":
        ex1 = add_user_table.objects.filter(id=id).update(
            user_name=request.POST['user_name'],
            email=request.POST['email'],
            registration=request.POST['registration'],
            designation=request.POST['designation'],
            status=request.POST['status'])

        messages.error(request, "Successfully updated!...", extra_tags="reservation_success")
        users = add_user_table.objects.all()
        return render(request, "userlst.html", {"users": users})
def delete_user_list(request,id):
    view_data = add_user_table.objects.get(id=id)
    view_data.delete()
    print('delete')
    messages.error(request, "Successfully deleted!...", extra_tags="delete_success")
    users = add_user_table.objects.all()
    return render(request, "userlst.html", {"users": users})


def forgot_password(request):
    return render(request, "forgot_password.html")


def faqs(request):
    return render(request, "faqs.html")
