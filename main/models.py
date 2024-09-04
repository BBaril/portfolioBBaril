from django.db import models


# ----------------------------------------------------------------------- # class model #
class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)
    
    def __str__(self):
        return self.name


# --------------------------------------------------------------------- # Project model #
class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    tags = models.ManyToManyField(Tag, related_name="projects")
    link = models.URLField(max_length=200, blank=True)
    
    def __str__(self):
        return self.title
    

# ------------------------------------------------------------------ # model for images #
class ProjectImage(models.Model):
    project = models.ForeignKey(
        Project, related_name="images", on_delete=models.CASCADE
    )
    image = models.ImageField(upload_to="project_images/")
    
    def  __str__(self):
        return f"{self.project.title} Image"
    