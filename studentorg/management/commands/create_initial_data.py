from django.core.management.base import BaseCommand
from faker import Faker
from studentorg.models import College, Program, Organization, Student, OrgMember

class Command(BaseCommand):
    help = 'Create initial data for the application (fresh start)'

    def handle(self, *args, **kwargs):
        # Delete existing data first
        self.clear_data()

        # Generate fresh data
        self.create_organization(10)   # 10 Organizations
        self.create_students(50)       # 50 Students
        self.create_membership(10)     # 10 OrgMemberships

    def clear_data(self):
        # Delete in order to respect ForeignKey dependencies
        OrgMember.objects.all().delete()
        Student.objects.all().delete()
        Organization.objects.all().delete()
        self.stdout.write(self.style.WARNING('Existing data cleared.'))

    def create_organization(self, count):
        fake = Faker()
        colleges = College.objects.all()
        for _ in range(count):
            Organization.objects.create(
                name=fake.company(),
                college=colleges.order_by('?').first() if colleges.exists() else None,
                description=fake.sentence()
            )
        self.stdout.write(self.style.SUCCESS(f'{count} organizations created successfully.'))

    def create_students(self, count):
        fake = Faker('en_PH')
        programs = Program.objects.all()
        if not programs.exists():
            self.stdout.write(self.style.WARNING('No programs found, skipping student creation.'))
            return
        for _ in range(count):
            Student.objects.create(
                student_id=f"{fake.random_int(2020,2025)}-{fake.random_int(1,8)}-{fake.random_number(digits=4)}",
                lastname=fake.last_name(),
                firstname=fake.first_name(),
                middlename=fake.last_name(),
                program=programs.order_by('?').first()
            )
        self.stdout.write(self.style.SUCCESS(f'{count} students created successfully.'))

    def create_membership(self, count):
        fake = Faker()
        students = Student.objects.all()
        organizations = Organization.objects.all()
        if not students.exists() or not organizations.exists():
            self.stdout.write(self.style.WARNING('No students or organizations found, skipping memberships.'))
            return
        for _ in range(count):
            OrgMember.objects.create(
                student=students.order_by('?').first(),
                organization=organizations.order_by('?').first(),
                date_joined=fake.date_between(start_date='-2y', end_date='today')
            )
        self.stdout.write(self.style.SUCCESS(f'{count} org memberships created successfully.'))
