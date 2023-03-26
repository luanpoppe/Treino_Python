import dearpygui.dearpygui as dpg
import dearpygui.demo as dpgdemo




dpg.create_context()


dpg.create_context()

with dpg.window(label="Tutorial"):
    dpg.add_button(label="Button 1")
    dpg.add_button(label="Button 2")
    var1 = dpg.add_input_text(label="Diz aê")
    dpg.add_button(label="OK")

dpg.create_viewport(title='Custom Title', width=600, height=400)
dpg.create_viewport(title='Custom 2', width=600, height=400)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
