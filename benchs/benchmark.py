#!/usr/bin/env python3

import abc
import os
import psutil
import subprocess
import time
import matplotlib.pyplot as plt
import importlib
import importlib.util
import logging


useLogScale = True
template = "general-ledger"
_logger = logging.getLogger(__name__)

# import the python file the template render function
path = "templates/" + template + ".py"
_logger.info(f"Using template: {path}")
spec = importlib.util.spec_from_file_location("render", path)
if spec is None:
    raise ImportError(f"Could not import {path}")

if spec.loader is None:
    raise ImportError(f"Could not import {path}")
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)
render = mod.render


def measure_command_usage(command):
    """
    Spawns a process via psutil, measures the time and peak memory usage.
    It attempts to include child processes in the memory measurement.
    Returns (elapsed_time_in_seconds, peak_memory_in_MB).
    """
    # Start time
    start_time = time.time()

    # Launch process
    process = psutil.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    peak_memory = 0

    # While the process is running, poll memory usage
    while True:
        if process.poll() is not None:
            # The process has finished
            break

        # Get memory usage of the process and all its children
        try:
            mem_info = process.memory_info().rss
            for child in process.children(recursive=True):
                mem_info += child.memory_info().rss
            if mem_info > peak_memory:
                peak_memory = mem_info
        except psutil.NoSuchProcess:
            pass

        time.sleep(0.05)  # Poll at 50ms intervals

    # Final check in case memory peaked right before the loop ended
    try:
        mem_info = process.memory_info().rss
        for child in process.children(recursive=True):
            mem_info += child.memory_info().rss
        if mem_info > peak_memory:
            peak_memory = mem_info
    except psutil.NoSuchProcess:
        pass

    # End time
    end_time = time.time()
    elapsed_time = end_time - start_time

    # Convert peak memory from bytes to MB
    peak_memory_mb = peak_memory / (1024.0 * 1024.0)

    return elapsed_time, peak_memory_mb


class Engine:
    @abc.abstractmethod
    def name(self) -> str: ...

    @abc.abstractmethod
    def command(self, input) -> list[str]: ...


class PaperMuncher(Engine):
    def name(self) -> str:
        return "paper-muncher"

    def command(self, input) -> list[str]:
        return [
            "paper-muncher",
            "print",
            input,
            "-o",
            "/dev/null",
            "--scale",
            "0.65x",
        ]


class Prince(Engine):
    def name(self) -> str:
        return "prince"

    def command(self, input) -> list[str]:
        return [
            "taskset",
            "-c",
            "0",
            "prince",
            input,
            "-o",
            "/dev/null",
        ]


class WkHtmlToPdf(Engine):
    def name(self) -> str:
        return "wkhtmltopdf"

    def command(self, input) -> list[str]:
        return [
            "wkhtmltopdf",
            "--quiet",
            "--enable-local-file-access",
            "--footer-html",
            "templates/footer.html",
            "--header-html",
            "templates/header.html",
            "--javascript-delay",
            "1000",
            input,
            "/dev/null",
        ]


class GoogleChrome(Engine):
    def name(self) -> str:
        return "Google Chrome"

    def command(self, input) -> list[str]:
        return [
            "google-chrome-stable",
            "--headless",
            "--disable-gpu",
            "--print-to-pdf=/dev/null",
            input,
        ]


class WeasyPrint(Engine):
    def name(self) -> str:
        return "weasyprint"

    def command(self, input) -> list[str]:
        return ["weasyprint", input, "/dev/null"]


ENGINES = [
    PaperMuncher(),
    WkHtmlToPdf(),
    Prince(),
    GoogleChrome(),
    WeasyPrint(),
]


def main() -> None:
    logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(message)s")

    table_sizes = [2**i for i in range(1, 12)]

    times: list[dict[str, float]] = []
    mems: list[dict[str, float]] = []

    for size in table_sizes:
        html_file = f"bench_{size}.xhtml"
        _logger.info("")
        _logger.info(f"Generating HTML document with {size} rows...")
        with open(html_file, "w") as f:
            render(size, f)

        times.append({})
        mems.append({})

        for engine in ENGINES:
            _logger.info(
                f"Measuring {engine.name()} performance for tableSize={size}..."
            )
            t, m = measure_command_usage(engine.command(html_file))
            _logger.info(f"{engine.name()}: time={t:.2f}s, memory={m:.2f}MB")
            times[-1][engine.name()] = t
            mems[-1][engine.name()] = m

        # Clean up HTML file if you want
        os.remove(html_file)

    # --- Plot results ---
    fig, (ax_time, ax_mem) = plt.subplots(1, 2, figsize=(12, 6))
    fig.suptitle(f"HTML to PDF Conversion Performance ({template} template)")
    # Time plot
    for engine in ENGINES:
        engine_times = [t[engine.name()] for t in times]
        ax_time.plot(table_sizes, engine_times, marker="o", label=engine.name())
    if useLogScale:
        ax_time.set_xscale("log")
        ax_time.set_xlabel("Table Size (log scale)")
        ax_time.set_yscale("log")
        ax_time.set_ylabel("Time (seconds, log scale)")
    else:
        ax_time.set_xlabel("Table Size")
        ax_time.set_ylabel("Time (seconds)")

    ax_time.set_title("Conversion Time")
    ax_time.legend()
    ax_time.grid(True)

    # Memory plot
    for engine in ENGINES:
        engine_mems = [m[engine.name()] for m in mems]
        ax_mem.plot(table_sizes, engine_mems, marker="o", label=engine.name())
    if useLogScale:
        ax_mem.set_xscale("log")
        ax_mem.set_xlabel("Table Size (log scale)")
        ax_mem.set_yscale("log")
        ax_mem.set_ylabel("Peak Memory (MB, log scale)")
    else:
        ax_mem.set_xlabel("Table Size")
        ax_mem.set_ylabel("Peak Memory (MB)")

    ax_mem.set_title("Peak Memory Usage")
    ax_mem.legend()
    ax_mem.grid(True)

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
