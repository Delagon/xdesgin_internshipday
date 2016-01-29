from __future__ import unicode_literals

from django.db import models

class Ship(models.Model):
  name = models.CharField(max_length=128, primary_key=True)
  manufacturer = models.CharField(max_length=128)
  cost_in_credits = models.BigIntegerField()
  length = models.BigIntegerField()
  max_atmosphering_speed = models.BigIntegerField()
  cargo_capacity_kg = models.BigIntegerField()
  hyperdrive_rating = models.IntegerField()
  docking_station_latitide = models.FloatField()
  docking_station_longitude = models.FloatField()
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

