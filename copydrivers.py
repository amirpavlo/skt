import bpy

class Drivers:
    """Copy Driver to destination object"""
    def __init__(self, src, dst):
        self.__src_obj = src
        self.__dst_obj = dst

    def __populate_modifier(self, src, dst):
        dst.active = src.active
        dst.blend_in = src.blend_in
        dst.blend_out = src.blend_out
        dst.influence = src.influence
        dst.mode = src.mode
        dst.mute = src.mute
        dst.poly_order = src.poly_order
        # type should be created when the modifier is created
        #mod.type = m['type']
        dst.use_additive = src.use_additive
        dst.use_influence = src.use_influence
        dst.coefficients[0] = src.coefficients[0]
        dst.coefficients[1] = src.coefficients[1]

    def __populate_modifiers(self, srcm, dstm):
        i = 0
        if len(srcm) <= 0 or len(dstm) <= 0:
            return
        mod = dstm[0]
        for m in srcm:
            if i == 0:
                self.__populate_modifier(m, mod)
                i = i + 1
            else:
                mod = dst.modifiers.new(m.type)
                self.__populate_modifier(m, mod)

    def __create_variable(self, var, driver):
        v = driver.driver.variables.new()

        v.name = var.name
        v.type = var.type

        # we have one target by default
        v.targets[0].id = var.targets[0].id
        v.targets[0].bone_target = var.targets[0].bone_target
        v.targets[0].data_path = var.targets[0].data_path
        v.targets[0].rotation_mode = var.targets[0].rotation_mode
        v.targets[0].transform_space = var.targets[0].transform_space
        v.targets[0].transform_type = var.targets[0].transform_type

    def copy(self):
        # iterate over all the shape key drivers in the source mesh
        num_drivers = 0
        for d in self.__src_obj.data.shape_keys.animation_data.drivers:
            print("--------->"+d.data_path)
            shape_name = d.data_path.replace('key_blocks["', '').replace('"].value', '')
            idx = self.__dst_obj.data.shape_keys.key_blocks.find(shape_name)
            if  idx == -1:
                print("Can't find shape key: %s" % (shape_name))
                continue
            # Copy driver but don't overwrite existing data
            #check = self.__dst_obj.data.shape_keys.animation_data and \
            #        self.__dst_obj.data.shape_keys.animation_data.drivers.find(d.data_path)
            #if check:
            #    print("%s has animation data" % (d.data_path))
            #    continue
            driver = self.__dst_obj.data.shape_keys.key_blocks[idx].driver_add('value')
            driver.hide = d.hide
            driver.lock = d.lock
            driver.mute = d.mute
            driver.select = d.select
            self.__populate_modifiers(d.modifiers, driver.modifiers)
            driver.driver.expression = d.driver.expression
            driver.driver.is_valid = d.driver.is_valid
            driver.driver.type = d.driver.type
            driver.driver.use_self = d.driver.use_self
            for var in d.driver.variables:
                self.__create_variable(var, driver)
            num_drivers += 1
        return num_drivers

