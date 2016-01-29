from __future__ import unicode_literals

from django.db import models

class Ship(models.Model):
  name = models.CharField(max_length=128, primary_key=True)
  manufacturer = models.CharField(max_length=128)
  cost_in_credits = models.BigIntegerField(default=0)
  length = models.BigIntegerField(default=0)
  max_atmosphering_speed = models.BigIntegerField(default=0)
  cargo_capacity_kg = models.BigIntegerField(default=0)
  hyperdrive_rating = models.FloatField(default=0)
  docking_station_latitide = models.FloatField(default=0)
  docking_station_longitude = models.FloatField(default=0)
  def to_json(self):
    s = "{"
    s += "\"name\":\"" + str(self.name) + "\","
    s += "\"manufacturer\":\"" + str(self.manufacturer) + "\","
    s += "\"cost_in_credits\":\"" + str(self.cost_in_credits) + "\","
    s += "\"length\":\"" + str(self.length) + "\","
    s += "\"max_atmosphering_speed\":\"" + str(self.max_atmosphering_speed) + "\","
    s += "\"cargo_capacity_kg\":\"" + str(self.cargo_capacity_kg) + "\","
    s += "\"hyperdrive_rating\":\"" + str(self.hyperdrive_rating) + "\","
    s += "\"docking_station_latitide\":\"" + str(self.docking_station_latitide) + "\""
    s += "\"docking_station_longitude\":\"" + str(self.docking_station_longitude) + "\"}"
    return s
  def setup(self, sa):
    self.manufacturer = sa[1]
    self.cost_in_credits = sa[2]
    self.length = sa[3]
    self.max_atmosphering_speed = sa[4]
    self.cargo_capacity_kg = sa[5]
    self.hyperdrive_rating = sa[6]
    self.docking_station_latitide = sa[7]
    self.docking_station_longitude = sa[8]
    self.save()

