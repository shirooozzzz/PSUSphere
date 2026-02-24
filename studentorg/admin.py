from django.contrib import admin
from .models import College, Program, Organization, Student, OrgMember


# -------------------------
# College Admin
# -------------------------
@admin.register(College)
class CollegeAdmin(admin.ModelAdmin):
    list_display = ("college_name", "created_at", "updated_at")
    search_fields = ("college_name",)
    list_filter = ("created_at",)


# -------------------------
# Program Admin
# -------------------------
@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
    list_display = ("prog_name", "college", "created_at")
    search_fields = ("prog_name", "college__college_name")
    list_filter = ("college",)


# -------------------------
# Organization Admin
# -------------------------
@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ("name", "college", "description", "created_at")
    search_fields = ("name", "description")
    list_filter = ("college",)


# -------------------------
# Student Admin
# -------------------------
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ("student_id", "lastname", "firstname", "middlename", "program")
    search_fields = ("lastname", "firstname")
    list_filter = ("program",)


# -------------------------
# OrgMember Admin
# -------------------------
@admin.register(OrgMember)
class OrgMemberAdmin(admin.ModelAdmin):
    list_display = ("student", "get_member_program", "organization", "date_joined")
    search_fields = ("student__lastname", "student__firstname")
    list_filter = ("organization",)

    def get_member_program(self, obj):
        return obj.student.program

    get_member_program.short_description = "Program"
