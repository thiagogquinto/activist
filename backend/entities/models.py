"""
Entities Models

This file contains models for the entities app.

TODO: All fields have on_delete=models.CASCADE: this needs to be reviewed, as SET_NULL is preferable in many cases.
TODO: Some relational-models may need to be moved in the "events" or "content" app in order to prevent circular dependency issues.
TODO: In some/most cases a "ManyToManyField" may be more suitable and scalable than "ArrayField"

Contents:
    - Organization
    - OrganizationApplicationStatus
    - OrganizationApplication
    - OrganizationEvent
    - OrganizationMember
    - OrganizationResource
    - Group
    - OrganizationTask
    - OrganizationTopic
    - GroupEvent
    - GroupMember
    - GroupResource
    - GroupTopic
"""

import uuid

from django.contrib.postgres.fields import ArrayField
from django.db import models

class OrganizationApplicationStatus(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    status_name = models.CharField(max_length=255)

    def __str__(self):
        return self.status_name


class OrganizationApplication(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    org_id = models.IntegerField(null=True)
    status = models.ForeignKey(
        "OrganizationApplicationStatus", on_delete=models.CASCADE
    )
    orgs_in_favor = ArrayField(models.IntegerField(null=True, blank=True), blank=True)
    orgs_against = ArrayField(models.IntegerField(null=True, blank=True), blank=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    status_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.creation_date

class Organization(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    tagline = models.CharField(max_length=255)
    social_accounts = ArrayField(models.CharField(max_length=255))
    total_flags = models.IntegerField(null=True)
    application_id = models.ForeignKey(OrganizationApplication, on_delete=models.CASCADE)
    created_by = models.ForeignKey(
        "authentication.User", related_name="created_orgs", on_delete=models.CASCADE
    )
    creation_date = models.DateTimeField(auto_now_add=True)
    deletion_date = models.DateField(null=True)

    def __str__(self):
        return self.name


class OrganizationEvent(models.Model):
    org_id = models.ForeignKey(Organization, on_delete=models.CASCADE)
    event_id = models.ForeignKey("events.Event", on_delete=models.CASCADE)

    def __str__(self):
        return self.id


class OrganizationMember(models.Model):
    org_id = models.ForeignKey(Organization, on_delete=models.CASCADE)
    user_id = models.ForeignKey("authentication.User", on_delete=models.CASCADE)
    is_owner = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_comms = models.BooleanField(default=False)

    def __str__(self):
        return self.id


class OrganizationResource(models.Model):
    org_id = models.ForeignKey(Organization, on_delete=models.CASCADE)
    resource_id = models.ForeignKey("content.Resource", on_delete=models.CASCADE)

    def __str__(self):
        return self.id


class Group(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    org_id = models.ForeignKey(Organization, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    tagline = models.CharField(max_length=255)
    description = models.TextField(max_length=500)
    social_accounts = ArrayField(models.CharField(max_length=255))
    total_flags = models.IntegerField(null=True)
    created_by = models.ForeignKey("authentication.User", on_delete=models.CASCADE)
    creation_date = models.DateTimeField(auto_now_add=True)
    deletion_date = models.DateField(null=True)

    def __str__(self):
        return self.name


class OrganizationTask(models.Model):
    org_id = models.ForeignKey(Organization, on_delete=models.CASCADE)
    task_id = models.ForeignKey("content.Task", on_delete=models.CASCADE)
    group_id = models.ForeignKey("Group", on_delete=models.CASCADE)

    def __str__(self):
        return self.id


class OrganizationTopic(models.Model):
    org_id = models.ForeignKey(Organization, on_delete=models.CASCADE)
    topic_id = models.ForeignKey("content.Topic", on_delete=models.CASCADE)

    def __str__(self):
        return self.id


class GroupEvent(models.Model):
    group_id = models.ForeignKey(Group, on_delete=models.CASCADE)
    event_id = models.ForeignKey("events.Event", on_delete=models.CASCADE)

    def __str__(self):
        return self.id


class GroupMember(models.Model):
    group_id = models.ForeignKey(Group, on_delete=models.CASCADE)
    user_id = models.ForeignKey("authentication.User", on_delete=models.CASCADE)
    is_admin = models.BooleanField(default=False)

    def __str__(self):
        return self.id


class GroupResource(models.Model):
    group_id = models.ForeignKey(Group, on_delete=models.CASCADE)
    resource_id = models.ForeignKey("content.Resource", on_delete=models.CASCADE)

    def __str__(self):
        return self.id


class GroupTopic(models.Model):
    group_id = models.ForeignKey(Group, on_delete=models.CASCADE)
    topic_id = models.ForeignKey("content.Topic", on_delete=models.CASCADE)

    def __str__(self):
        return self.id
