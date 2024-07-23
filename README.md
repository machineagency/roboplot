# roboplot

On July 23rd 2024 the Agents had fun plotting with the xArm6

## Resources

- xArm SDK: https://github.com/xArm-Developer/xArm-Python-SDK

## Instructions

1. install the xArm API:
   `https://github.com/xArm-Developer/xArm-Python-SDK/tree/master`
2. Plug in ethernet cable and configure the wired connection in your OS
   settings:
   1. Choose IPV4, configure manually:
   2. IP addresss: 192.168.1.12
   3. Subnet mask: 255.255.255.0
   4. default gateway: 192.168.1.1
   5. DNS server: 192.168.1.1
3. install vpype: https://vpype.readthedocs.io/en/latest/install.html
4. install the gcode plugin: https://github.com/plottertools/vpype-gcode
5. also install `matplotlib` and `numpy`
6. generate example csv:
   `vpype --config gwriteConfig.toml rect 0mm 0mm 10mm 10mm gwrite -p custom square.csv `
7. run the script: `python3 arm_plot.py`
