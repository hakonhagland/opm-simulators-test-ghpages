/*
  Copyright 2024 Equinor ASA.

  This file is part of the Open Porous Media project (OPM).

  OPM is free software: you can redistribute it and/or modify
  it under the terms of the GNU General Public License as published by
  the Free Software Foundation, either version 3 of the License, or
  (at your option) any later version.

  OPM is distributed in the hope that it will be useful,
  but WITHOUT ANY WARRANTY; without even the implied warranty of
  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
  GNU General Public License for more details.

  You should have received a copy of the GNU General Public License
  along with OPM.  If not, see <http://www.gnu.org/licenses/>.
*/

#ifndef OPM_PY_BLACKOIL_SIMULATOR_DOC_HEADER_INCLUDED
#define OPM_PY_BLACKOIL_SIMULATOR_DOC_HEADER_INCLUDED

namespace Opm::Pybind::DocStrings {

// Constructors
// ------------

static constexpr char PyBlackOilSimulator_filename_constructor_docstring[] = R"doc(
// Signature: __init__(deck_filename: str) -> None

Constructor using a deck file name.

:param deck_filename: The file name of the deck to be used for the simulation.
:type deck_filename: str
)doc";

static constexpr char PyBlackOilSimulator_objects_constructor_docstring[] = R"doc(
// Signature: __init__(deck: Deck, state: EclipseState, schedule: Schedule, summary_config: SummaryConfig) -> None

Constructor using Deck, EclipseState, Schedule, and SummaryConfig objects.

:param deck: Deck object.
:type deck: Deck
:param state: EclipseState object.
:type state: EclipseState
:param schedule: Schedule object.
:type schedule: Schedule
:param summary_config: SummaryConfig object.
:type summary_config: SummaryConfig
)doc";


// Methods in alphabetic order
// ----------------------------

static constexpr char advance_docstring[] = R"doc(
// Signature: advance(report_step: int) -> None

Advance the simulation to a specific report step.

:param report_step: Target report step to advance to.
:type report_step: int
)doc";

static constexpr char checkSimulationFinished_docstring[] = R"doc(
// Signature: check_simulation_finished() -> bool

Check if the simulation has finished.

:return: True if the simulation is finished, False otherwise.
)doc";

static constexpr char currentStep_docstring[] = R"doc(
// Signature: current_step() -> int

Get the current simulation step.

:return: The current step number.
)doc";

static constexpr char getCellVolumes_docstring[] = R"doc(
// Signature: get_cell_volumes() -> numpy.ndarray

Retrieve the cell volumes of the simulation grid.

:return: An array of cell volumes.
:type return: numpy.ndarray
)doc";

static constexpr char getDT_docstring[] = R"doc(
// Signature: get_dt() -> float

Get the timestep size of the last completed step.

:return: Timestep size in days.
:type return: float
)doc";

static constexpr char getPorosity_docstring[] = R"doc(
// Signature: get_porosity() -> numpy.ndarray

Retrieve the porosity values of the simulation grid.

:return: An array of porosity values.
:type return: numpy.ndarray
)doc";

static constexpr char run_docstring[] = R"doc(
// Signature: run() -> int

Run the simulation with the provided deck file or previously set deck.

:return: EXIT_SUCCESS if the simulation completes successfully.
)doc";

static constexpr char setPorosity_docstring[] = R"doc(
// Signature: set_porosity(porosity: numpy.ndarray) -> None

Set the porosity values for the simulation grid.

:param porosity: An array of porosity values to be set.
:type porosity: numpy.ndarray
)doc";

static constexpr char step_docstring[] = R"doc(
// Signature: step() -> int

Execute the next simulation report step.

:return: Result of the simulation step.
)doc";

static constexpr char stepCleanup_docstring[] = R"doc(
// Signature: step_cleanup() -> int

Perform cleanup after a simulation step.

:return: EXIT_SUCCESS if cleanup is successful.
)doc";

static constexpr char stepInit_docstring[] = R"doc(
// Signature: step_init() -> int

Initialize the simulation step.

:return: EXIT_SUCCESS if the initialization is successful.
)doc";

} // namespace Opm::Pybind::DocStrings

#endif // OPM_PY_BLACKOIL_SIMULATOR_DOC_HEADER_INCLUDED
