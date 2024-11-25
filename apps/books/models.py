from django.utils.translation import gettext_lazy as _
from django.db import models

class Author(models.Model):
    full_name = models.CharField(_("Full name"), max_length=255)
    bio = models.TextField(_("Bio"))
    
    class Meta:
        verbose_name = _("Author")
        verbose_name_plural = _("Authors")

class Book(models.Model):
    title = models.CharField(_("Title"), max_length=255)
    description = models.TextField(_("Description"))
    cover = models.ImageField(_("Cover"), upload_to="covers")
    author = models.ForeignKey(
        to="Author", 
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="books",
        verbose_name=_("Author")
    )
    quantity = models.IntegerField(_("Quantity"), default=0)
    price = models.DecimalField(_("Price"), max_digits=12, decimal_places=2)
    
    class Meta:
        verbose_name = _("Book")
        verbose_name_plural = _("Books")
        
    @staticmethod
    def generate_fake():
        from faker import Faker
        from random import choice, randint
        fake = Faker()

        def create_authors(num_authors=10):
            authors = []
            for _ in range(num_authors):
                author = Author(
                    full_name=fake.name(),
                    bio=fake.text(max_nb_chars=500)
                )
                authors.append(author)
            Author.objects.bulk_create(authors)
            print(f"{num_authors} authors created.")

        def create_books(num_books=50):
            authors = list(Author.objects.all())
            books = []
            for _ in range(num_books):
                book = Book(
                    title=fake.sentence(nb_words=5),
                    description=fake.text(max_nb_chars=1000),
                    cover=None,
                    author=choice(authors) if authors else None,
                    quantity=randint(1, 100),
                    price=round(randint(5, 100) + fake.random_number(digits=2) / 100, 2)
                )
                books.append(book)
            Book.objects.bulk_create(books)
            print(f"{num_books} books created.")

        create_authors(100)
        create_books(500)

class BookReview(models.Model):
    book = models.ForeignKey("Book", on_delete=models.PROTECT, related_name="reviews")
    rate = models.PositiveSmallIntegerField(default=0)
    comment = models.TextField()
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    
    @staticmethod
    def create_fake_book_reviews(num_reviews=10):
        import random
        from faker import Faker 
        from apps.users.models import User
        fake = Faker()
        
        users = list(User.objects.all())
        books = list(Book.objects.all())

        if not users or not books:
            print("No users or books available in the database.")
            return

        for _ in range(num_reviews):
            user = random.choice(users)
            book = random.choice(books)
            rate = random.randint(1, 5)
            review = fake.paragraph(nb_sentences=5)

            BookReview.objects.create(
                book=book,
                rate=rate,
                review=review,
                user=user,
            )

        print(f"{num_reviews} fake book reviews created successfully!")



    

    @staticmethod
    def create_fake_users(count=1):
        from faker import Faker
        from apps.users.models import User
        fake = Faker()
        users = []
        
        for _ in range(count):
            # Generate a unique username
            username = fake.user_name()
            while User.objects.filter(username=username).exists():
                username = fake.user_name()

            email = fake.email()
            password = fake.password()
            role = fake.random_element([("User", "Salesman")])  # Ensure the role selection is valid
            phone_number = fake.phone_number()

            # Create and save the user
            user = User.objects.create(
                username=username,
                email=email,
                password=password,
                role=role,
                phone_number=phone_number
            )
            users.append(user)
        
        return users