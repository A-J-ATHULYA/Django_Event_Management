from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic import View
from .models import Event, Organizer, Participant

# Create your views here.

#Welcome API

class WelcomeView(View):
    def get(self, request):
        data = {
            "Message": "Welcome to Event Management System..!"
        }
        return JsonResponse(data)


#Organization Information API

class OrganizationView(View):
    def get(self, request):
        data = {
            "Organization_Name": "Dream Events",
            "Location": "Kochi",
            "Contact": "9876543210",
            "Email": "dreamevents@gmail.com",
            "Status": "Active"
        }
        return JsonResponse(data)


#Event Information API

class EventView(View):
    def get(self, request):
        data = {
            "Event_ID": 101,
            "Event_Name": "Tech Fest 2026",
            "Event_Type": "Technology",
            "Location": "Kochi",
            "Event_Date": "2026-12-15",
            "Ticket_Price": 500,
            "Status": "Available"
        }
        return JsonResponse(data)


#Organizer Information API

class OrganizerView(View):
    def get(self, request):
        organizers = Organizer.objects.all()

        data = []

        for organizer in organizers:
            data.append({
                "id": organizer.id,
                "name": organizer.name,
                "email": organizer.email,
                "contact": organizer.contact,
                "organization": organizer.organization,
                "location": organizer.location
            })

        return JsonResponse({"Organizers": data})


#All Events API

class AllEventsView(View):
    def get(self, request):
        data = {
            "Events": [
                {
                    "Event_ID": 101,
                    "Event_Name": "Tech Fest",
                    "Event_Type": "Technology",
                    "Location": "Kochi",
                    "Ticket_Price": 500
                },
                {
                    "Event_ID": 102,
                    "Event_Name": "Music Festival",
                    "Event_Type": "Music",
                    "Location": "Alappuzha",
                    "Ticket_Price": 300
                },
                {
                    "Event_ID": 103,
                    "Event_Name": "Food Carnival",
                    "Event_Type": "Food",
                    "Location": "Thrissur",
                    "Ticket_Price": 200
                },
                {
                    "Event_ID": 104,
                    "Event_Name": "Art Exhibition",
                    "Event_Type": "Art",
                    "Location": "Kozhikode",
                    "Ticket_Price": 150
                }
            ]
        }

        return JsonResponse(data)


# API 6 - Participant Information API

class ParticipantView(View):
    def get(self, request):
        participants = Participant.objects.all()

        data = []

        for participant in participants:
            data.append({
                "id": participant.id,
                "name": participant.name,
                "email": participant.email,
                "contact": participant.contact,
                "event_name": participant.event_name,
                "ticket_count": participant.ticket_count
            })

        return JsonResponse({"Participants": data})


#Venue Information API

class VenueView(View):
    def get(self, request):
        data = {
            "Venue_Name": "Grand Auditorium",
            "Location": "Kochi",
            "Capacity": 1000,
            "Parking": "Available",
            "Facilities": [
                "AC",
                "Projector",
                "Sound System",
                "Parking"
            ],
            "Status": "Available"
        }

        return JsonResponse(data)