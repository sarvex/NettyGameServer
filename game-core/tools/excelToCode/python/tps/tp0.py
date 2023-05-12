
import math

def use_origin(arg): return arg
def use_empty(arg): return None

def to_bool(arg):
	if not isinstance(arg, (unicode, str)):
		return bool(arg)
	if arg == "false":
		return False
	elif arg == "true":
		if arg == "true": return True
	return bool(to_int(arg))

def to_int(arg):
	return int(to_float(arg))

def to_float(arg):
	return 0 if arg == "" else float(arg)

def to_str(value):
	if type(value) == unicode:
		return value.encode("utf-8")
	elif type(value) != str:
		return str(value)
	return value

def to_list(arg, converter=None):
	ret = eval(f"[{arg}]")
	if not isinstance(ret, list):
		raise (ValueError, f"list type needed, '{arg}' was given")

	if converter is not None:
		for i, v in enumerate(ret):
			ret[i] = converter(v)

	return ret

def to_int_list(arg): return to_list(arg, to_int)
def to_float_list(arg): return to_list(arg, to_float)

# arg = "a:b, c:d"
def to_dict(arg):
	if type(arg) != unicode:
		raise ValueError, "string type needed."

	return eval("{%s}" % arg)

# args = "a,b; c,d;"
def to_dict2(args, func = to_float_list):
	lst = args.split(';')
	ret = {}
	for st in lst:
		st = st.strip()
		if len(st) == 0: continue

		values = func(st)
		if len(values) != 2:
			raise (ValueError, f"invalid fontal {args}")

		k, v = values
		ret[k] = v
	return ret

def to_point(arg):
	lst = to_float_list(arg)
	if len(lst) != 2:
		raise (ValueError, f"point type need 2 float elemnt, '{arg}' was given")
	return tuple(lst)

def to_point3(arg):
	lst = to_float_list(arg)
	if len(lst) != 3:
		raise (ValueError, f"point3 type need 3 float element, '{arg}' was given")
	return tuple(lst)

def to_point_list(args):
	ret = []
	groups = args.split(';')
	for group in groups:
		group = group.strip()
		if len(group) == 0: continue

		ret.append(to_point(group))

	return ret


def to_point3_list(args):
	ret = []
	groups = args.split(';')
	for group in groups:
		group = group.strip()
		if len(group) == 0: continue

		ret.append(to_point3(group))

	return ret

def to_string_list(args):
	ret = []

	images = args.split(',')
	for image in images:
		image = image.strip()
		if len(image) > 0:
			ret.append(image)

	return ret if ret else None

def to_float_group(args):
	ret = []

	groups = args.split(';')
	for group in groups:
		group = group.strip()
		if len(group) == 0: continue

		ret.append(to_float_list(group))

	return ret

def to_images(args):
	ret = to_string_list(args)
	return [f"{x}.png" for x in ret] if ret != None else ret

def to_float_list_2(args):
	if type(args) != unicode: return None
	ret = []

	groups = args.split(';')
	for group in groups:
		group = group.strip()
		if len(group) == 0: continue

		ret.append(to_float(group))

	return ret

def to_string_list_2(args):
	ret = []

	images = args.split(';')
	for image in images:
		image = image.strip()
		if len(image) > 0:
			ret.append(image)

	return ret if ret else None

def to_text(args):
	return args.replace('\n','\\n')

def to_amstr(args):
	return f"{args}.am"

def type2string(tp):
	if tp in [int, long, to_int]: return "int"
	if tp in [float, to_float]: return "float"
	return "byte" if tp in [to_bool, bool] else "String"
