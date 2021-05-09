import ModelGlobalVar as gl
import ModuleSimple
import ModuleCreep
import ModuleCrack

#启动文件 
if __name__ == "__main__":
    simple = gl.get_value('model_1')
    creep = gl.get_value('model_2')
    crack = gl.get_value('model_3')
    for i in [simple, creep, crack]:
        print(i+' OK!')
     

