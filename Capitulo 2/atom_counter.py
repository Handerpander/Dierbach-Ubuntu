# Your place in the Universe Program

# This program will determine the approximate numbre of atoms that a
# person consists of and the percent of the universe that they comprise.

# initialization
num_atoms_universe = 10e80
weight_avg_person = 70 # 70 kg (154 lbs)
num_atoms_avg_person = 7e27

#program greeting
print('This program will determine your place in the universe.')

#prompt for user's weight
weight_lbs = int(input('Enter your weight in pound: '))

# convert weight to kilograms
weight_kg = 2.2 * weight_lbs

# determine number atoms in person
num_atoms = (weight_kg / 70) * num_atoms_avg_person
percent_of_universe = (num_atoms / num_atoms_universe) * 100

# display results
print('You contain approximately', format(num_atoms, '.2e'), 'atoms')
print('THerefore, you comprise', format(percent_of_universe, '.2e'),
      '% of the universe')