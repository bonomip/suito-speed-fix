# Elite Suito Speed Bug fix

This is a soft fix that gives pretty realistic results. The actual speed is derived from [this](https://www.gribble.org/cycling/power_v_speed.html).

## Usage

Fist you need to manually change your weight inside bmath/mathbike.py (the variable is called weight, it's the first variable of the script you cannot miss that)

then launch the script from the comand line

```
python main.py path_to_incorrect_file.tcx
```

The output file will be create in the same folder of the input file under the name "file_fixed.tcx"
