# Copyright 2024 Stu Teasdale
# Redistribution and use in source and binary forms, with or without modification, are permitted
# under the conditions specified in the LICENSE file.

from random import randrange
ServiceGroups=[
	'Armed Forces (Military)',
	'Central Processing Unit',
	'HPD&MC',
	'IntSec',
	'PLC',
	'Power Services',
	'R&D',
	'Technical Services'
]

SecretSocieties=[
# Name, +2 skill, -2 skill
	('Antimutant', 'Intimidate', 'Bluff'),
	('Communists', 'Stealth', 'Charm'),
	('Corpore Metal', 'Program', 'Psychology'),
	('Death Leopard', 'Throw', 'Engineer'),
	('FCCCP', 'Psychology', 'Science'),
	('Frankenstein Destroyers', 'Melee', 'Program'),
	('Free Enterprise', 'Bluff', 'Bureaucracy'),
	('Haxxor', 'Operate', 'Melee'),
	('Psion', 'Science', 'Athletics'),
	('PURGE', 'Demolitions', 'Stealth'),
	('Romantics', 'Bureaucracy', 'Intimidate'),
	('Sierra Club', 'Athletics', 'Alpha Complex')
]

class Character:

	def __init__(self):
		self.profile={
			'Brains': { 'skills': {'Alpha Complex': 0, 'Bureaucracy': 0, 'Psychology': 0, 'Science': 0}, 'total': 0},
			'Chutzpah': { 'skills': {'Bluff': 0, 'Charm': 0, 'Intimidate': 0, 'Stealth': 0}, 'total': 0},
			'Mechanics': { 'skills': {'Demolitions': 0, 'Engineer': 0, 'Operate': 0, 'Program': 0}, 'total': 0},
			'Violence': { 'skills': {'Athletics': 0, 'Guns': 2, 'Melee': 0, 'Throw': 0}, 'total': 0},
		}


		self.all_skills = []
		for entry in self.profile.values():
			for k in entry['skills'].keys():
				self.all_skills.append(k)

		self.initial_skills = self.all_skills
		self.initial_skills.remove("Guns")

		for value in range(1,6):
			self.setInitialSkillValues(value)
			self.setInitialSkillValues(0-value)

		self.setServiceGroup()
		self.setSecretSociety()
		self.setSkillTotals()

	def _skillToCategory(self, skill):
		for group,entry in self.profile.items():
			if skill in entry['skills'].keys():
				return group
		return None
				

	def setServiceGroup(self):
		self.serviceGroup = ServiceGroups[randrange(0, len(ServiceGroups))]

	def setSecretSociety(self):
		ss = SecretSocieties[randrange(0, len(SecretSocieties))]

		self.secretSociety = ss[0]
		self.setSkillValue(ss[1], 2)
		self.setSkillValue(ss[2], -2)
		
		pass
	
	def setInitialSkillValues(self, value):

		#Remove guns from the list
		skill_idx = randrange(0,len(self.initial_skills))
		
		s = self.initial_skills[skill_idx]
		self.setSkillValue(s, value)
		del self.initial_skills[skill_idx]

	def setSkillValue(self, skill, value):
		c = self._skillToCategory(skill)
		self.profile[c]['skills'][skill] += value
		if self.profile[c]['skills'][skill] < -5:
			self.profile[c]['skills'][skill] = -5
		if self.profile[c]['skills'][skill] > 5:
			self.profile[c]['skills'][skill] = 5

	def setSkillTotals(self):
		for group, entry in self.profile.items():
			for v in entry['skills'].values():
				self.profile[group]['total'] += v
			if self.profile[group]['total'] < -5:
				self.profile[group]['total'] = -5
			if self.profile[group]['total'] > 5:
				self.profile[group]['total'] = 5
	
	def getCategories(self):
		return list(self.profile.keys())
	
	def getCategorySkillsValues(self,category):
		return list(self.profile[category]['skills'].items())

	def printCharacter(self):
		profile = self.profile
		spacing = ' '*8

		print('------------------------------------')
		print()
		print("Service Group: {}".format(self.serviceGroup))
		print()
		print("Secret Society: {}".format(self.secretSociety))
		print()

		o = []
		for c in self.getCategories():
			o.append("{:<16} {:>2}".format(c+':', profile[c]['total']))

		print(spacing.join(o))
		print()
		print(profile)
		for i in range(0,4):
			o = []
			for c in self.getCategories():
				skills = self.getCategorySkillsValues(c)
				o.append("{:<16} {:>2}".format(skills[i][0],skills[i][1]))
			print(spacing.join(o))


if __name__ == "__main__":
	char=Character()

	char.printCharacter()
