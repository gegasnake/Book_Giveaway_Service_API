# Book Giveaway Service API

# Objective:
The Book Giveaway Service API aims to facilitate the exchange of books among users. Registered users can offer books for free and take books offered by others. Non-registered users can view the available books. The project encompasses user registration, book management, and support for additional resources such as authors, genres, book conditions, and pickup locations.

# Core Features:

User Authentication: Users can register with email to access the service.
Books Management: CRUD operations for managing books.
Filtering: Ability to filter books based on various parameters like author, genre, etc.
Supporting Resources Management: Manage authors, genres, book conditions, images, and posters.
Book Retrieval Information: Include information on the location from where the book can be picked up.
Ownership Decision: Owners can choose the recipient if multiple users are interested in a book.

# Tech Stack:

Python with Flask/Django/FastAPI
PostgreSQL/SQLite as the database
RESTful API
Git
README with setup instructions
Swagger for API Documentation (Bonus)
Docker & Docker Compose (Bonus)
Deliverables:

Source code in a public GitHub repository.
API documentation using Swagger.
Docker and Docker Compose files for containerization.
A comprehensive README containing setup and running instructions.

# Bonus:

Swagger for API documentation.
Containerization with Docker & Docker Compose.
Unit tests (Only for demonstration).
Evaluation Criteria:

Code Quality
Feature Completeness
Documentation Quality
Ease of Setup (Docker, README)


# Resources I used to create this project:
1. First Question I had was: what is the difference between rebase and merge?
The main difference is that when we have Branch A and Branch B with some commits, rebase makes all the commits linear
and it adds all existing commits to one branch, however merge takes the last two commits made in branch A and B and it
merges them and creates a new merge commit which will be the continuation of the prior commits.
https://www.youtube.com/watch?v=0chZFIZLR_0
2. How can I configure and containerize the whole project? firstly, I had to create a dockerfile in which I specified
the version of python I use, then I put the installation of requirements.txt file packages so that every time I run the
image it installs all the new packages. In addition, I added the command to run the django server. Other than a dockerfile,
I used docker-compose.yml which describes a docker Compose configuration for a service named "Django".
https://www.youtube.com/watch?v=BoM-7VMdo7s
3. 