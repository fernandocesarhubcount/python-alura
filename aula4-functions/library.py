def define_invite_name(name):
	pos_final	= len(name)
	pos_initial = pos_final-4
	first_part  = name[0:4]
	second_part = name[pos_initial:pos_final]
	return first_part+second_part