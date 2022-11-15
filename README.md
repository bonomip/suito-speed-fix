# Elite Suito Speed Bug fix

This is a soft fix that gives pretty realistic results. The actual speed is derived from [this](https://www.gribble.org/cycling/power_v_speed.html) formula.

## Usage

Fist you need to manually change your [weight](https://github.com/bonomip/suito-speed-fix/blob/00418c87a50656d0e541ceb612f8fee1c193018a/bmath/mathbike.py#L3-L4) inside bmath/mathbike.py.

then launch the script from the comand line

```
python main.py path_to_incorrect_file.tcx
```

The output file will be create in the same folder of the input file under the name "file_fixed.tcx"
