# fys+修复了换行符 EOL 定义错误，使用原始字符串处理路径
EOL = '\n'
path_free_lib=r'D:\name_and_rebuild\FreeCAD\lib'
SOL = f'import sys{EOL}sys.path.append(r"{path_free_lib}"){EOL}import FreeCAD as App{EOL}import Part{EOL}'
RECOMPUTE = 'App.ActiveDocument.recompute()' + EOL
CHECK_MAKE_WIRE="""
    
"""