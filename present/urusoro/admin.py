from typing import Any
from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Personne)
class PersonneAdmin(admin.ModelAdmin):
    list_display= "nom", "prenom", "salaire", "created_by", "created_at", "date_adhesion"
    actions=["marquer_comme_present", "doubler"]
    
    def save_model(self, request, obj, form, change):
        obj. created_by=request.user
        obj.save()

    def marquer_comme_present(self, request, personnes):
            for umuntu in personnes: 
                  Presence(personne= umuntu, present=True, created_by=request.user).save()

    marquer_comme_present.short_description = "marquer ces gens comme present aujourd'hui"

    def doubler(self, request, personnes):
         for personne in personnes:
              personne.salaire = personne.salaire * 2 
              personne.save()

@admin.register(Presence)
class PresenceAdmin(admin.ModelAdmin):
    list_display= "personne", "present", "created_by", "created_at"
    actions=["remarquer_comme_present"]

    def save_model(self, request, obj, form, change) :
        obj.created_by = request.user
        obj.save()

    def remarquer_presence(self, request, personnes):
            for personneAdmin in personnes: 
                personneAdmin.present=False
                personneAdmin.save()


    remarquer_presence.short_description = "remarquer presence"

@admin.register(Salaire)
class SalaireAdmin(admin.ModelAdmin):
     list_display= "personne", "montant", "created_by", "created_at"
     actions= ["add_salary"]

     def save_model(self, request, obj, form, change):
          Personne = obj.personne
          nb_presence = Presence.objects.filter(personne = Personne).count()
          obj.montant = nb_presence * Personne.salaire
          obj.created_by = request.user
          obj.save()





