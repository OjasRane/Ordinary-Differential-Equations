# Animation examples

The scripts in this directory use the project's solvers to calculate trajectories, then display them with Matplotlib's `FuncAnimation`. The Python demos use the [`solver.ivp`](../solver/README.md) methods. Pre-rendered GIF and MP4 files are stored in [`animations/`](animations/).

## Gallery

| Example | Python source | Rendered animation |
| --- | --- | --- |
| Simple pendulum | [`pysolved/simple_pendulum.py`](pysolved/simple_pendulum.py) | [`simple_pendulum.gif`](animations/simple_pendulum.gif) |
| Undamped spring–mass system | [`pysolved/spring_mass.py`](pysolved/spring_mass.py) | [`spring_mass.gif`](animations/spring_mass.gif) |
| Damped spring–mass system | [`pysolved/damped_shm.py`](pysolved/damped_shm.py) | [`damped_shm.mp4`](animations/damped_shm.mp4) |
| Population model with the Allee effect | [`pysolved/population_modelling.py`](pysolved/population_modelling.py) | [`population_modelling.gif`](animations/population_modelling.gif) |
| Error function | [`pysolved/erf.py`](pysolved/erf.py) | [`erf.gif`](animations/erf.gif) |
| Double pendulum | [`pysolved/double_pendulum.py`](pysolved/double_pendulum.py) | [`double_pendulum.mp4`](animations/double_pendulum.mp4) |
| Lorenz attractor | [`pysolved/lorenz_attractor.py`](pysolved/lorenz_attractor.py) | [`lorenz_attractor.mp4`](animations/lorenz_attractor.mp4) |
| Nearby Lorenz trajectories | [`pysolved/two_lorenz_trajectories.py`](pysolved/two_lorenz_trajectories.py) | [`two_lorenz_trajectories.mp4`](animations/two_lorenz_trajectories.mp4) |
| Halvorsen attractor (C++ integration) | [`csolved/halvorsen_attractor/`](csolved/halvorsen_attractor/) | [`halvorsen_attractor.mp4`](animations/halvorsen_attractor.mp4) |

## Run a Python demo

Install the Python project using the [root setup guide](../README.md#python-setup). From the repository root, run a script such as:

```bash
uv run python animation_scripts/pysolved/simple_pendulum.py
```

Replace the script path with another Python source from the gallery. Each script computes the full numerical solution before opening an interactive Matplotlib window. A graphical Matplotlib backend is required. The scripts display the animation and do not save a new file by default.

## C++ Halvorsen attractor

The C++ example integrates the Halvorsen system and saves its time and state arrays in Jacobi's `.jcbi` format. The executable writes these files to its current working directory, while `animator.py` reads them from its current working directory. Build the `HalvorsenAttractor` target from the repository root:

```bash
cmake --build build --target HalvorsenAttractor
```

Run the executable from its Ninja build directory, then move the generated files to the example source directory. On Linux or macOS:

```bash
cd build/animation_scripts/csolved/halvorsen_attractor

./HalvorsenAttractor

cd ../../../../

mv build/animation_scripts/csolved/halvorsen_attractor/double_halvorsen_attractor_time.jcbi animation_scripts/csolved/halvorsen_attractor/

mv build/animation_scripts/csolved/halvorsen_attractor/double_halvorsen_attractor_solution.jcbi animation_scripts/csolved/halvorsen_attractor/

cd animation_scripts/csolved/halvorsen_attractor

uv run python animator.py
```

On Windows PowerShell, use:

```powershell
Set-Location build/animation_scripts/csolved/halvorsen_attractor

.\HalvorsenAttractor.exe

Set-Location ..\..\..\..

Move-Item -Force build/animation_scripts/csolved/halvorsen_attractor/double_halvorsen_attractor_time.jcbi animation_scripts/csolved/halvorsen_attractor/

Move-Item -Force build/animation_scripts/csolved/halvorsen_attractor/double_halvorsen_attractor_solution.jcbi animation_scripts/csolved/halvorsen_attractor/

Set-Location animation_scripts/csolved/halvorsen_attractor

uv run python animator.py
```

The `.jcbi` files are generated outputs and can be recreated by running the executable again.

The C++ build requires Jacobi at the paths documented in the C++ guide.

## Saving an animation

To export a modified Python animation, call `.save(...)` on its `FuncAnimation` object before `plt.show()`:

```python
anim.save("animation_scripts/animations/output.gif", writer="pillow", fps=30)
```

For MP4 output, use `writer="ffmpeg"` and ensure FFmpeg is installed. Some scripts name their animation object `ani` rather than `anim`. GIF export requires Matplotlib's Pillow writer. Exporting can take additional time and memory.

## Related guides

- [Python solver](../solver/README.md)
- [Analysis notebooks](../analysis/README.md)
- [C++ solver](../csolver/README.md)

## Project tree

```text
animation_scripts/
├── animations/                   # Pre-rendered GIF and MP4 files
├── csolved/
│   └── halvorsen_attractor/      # C++ simulation and Python animator
├── pysolved/                     # Python animation scripts
└── README.md                     # Animation guide
```

## License

The scripts and rendered files are part of the project distributed under the [MIT License](../LICENSE).
