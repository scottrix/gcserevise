#!/usr/bin/env python3
"""Insert missing AQA required-practical boxes (P1: practicals 1:1 with spec).
Separate sciences carry RP numbers; combined boxes name the practical only
(8464 numbering differs per science — avoid stating numbers we cannot verify).
Run: python3 content_practicals.py"""
from expand_topics import insert_before_section

RP = lambda title, steps, errs: (
    '<section class="section"><h2>🔬 Required Practical</h2>'
    f'<div class="required-practical"><h3>{title}</h3><ol>{steps}</ol>'
    f'<div class="key-point"><strong>Common errors:</strong> {errs}</div></div></section>')
LI = lambda t: f'<li>{t}</li>'

JOBS = {
    "topics/chemistry/aqa/C14-electrolysis.html": RP(
        "Electrolysis of Aqueous Solutions (AQA RP3)",
        LI("Set up a beaker with the test solution (e.g. sodium chloride or copper(II) sulfate solution) and two inert electrodes (graphite or platinum) connected to a low-voltage DC supply")
        + LI("Switch on and observe each electrode for bubbles or solid deposits for several minutes")
        + LI("Collect any gas at each electrode in a test tube and identify it: hydrogen relights a burning splint with a squeaky pop; oxygen relights a glowing splint; chlorine bleaches damp blue litmus paper")
        + LI("Record which product forms at the cathode (negative) and the anode (positive)")
        + LI("Repeat with a different solution to compare products")
        + LI("State your variables: solution type (independent), products observed (dependent), voltage and electrode type (controls)"),
        "electrodes touching (short circuit); voltage too low to produce observable products; confusing the electrodes — remember cathode = negative = reduction"),
    "topics/chemistry/aqa/C15-exothermic-and-endothermic-reactions.html": RP(
        "Temperature Changes in Reactions (AQA RP4)",
        LI("Place a fixed volume of dilute acid in a polystyrene cup with a lid, and record its starting temperature")
        + LI("Add a measured amount of the second reactant (e.g. metal powder or alkali), fit the lid with a thermometer through it, and stir gently")
        + LI("Record the maximum (or minimum) temperature reached")
        + LI("Calculate the temperature change (ΔT = final − initial): a rise is exothermic, a fall is endothermic")
        + LI("Repeat with different concentrations to investigate the effect on ΔT")
        + LI("Variables: concentration (independent), maximum temperature change (dependent), volumes and starting temperatures (controls)"),
        "heat loss without the lid and polystyrene cup; recording the temperature too late (the maximum passes quickly); unequal starting temperatures between trials"),
    "topics/physics/aqa/P2-conservation-and-efficiency.html": RP(
        "Thermal Insulation Factors (AQA RP2)",
        LI("Heat a fixed volume of water (e.g. 100 cm³) to a set starting temperature (e.g. 80 °C) and pour it into a container")
        + LI("Wrap the container in the first insulating material and thickness, and fit a lid")
        + LI("Record the water temperature every minute for 10 minutes")
        + LI("Repeat with the same water volume and starting temperature, changing only the insulator (or its thickness)")
        + LI("Plot cooling curves (temperature against time) for each material and compare the gradients")
        + LI("Variables: insulating material and thickness (independent), rate of temperature fall (dependent), water volume and starting temperature (controls)"),
        "changing more than one variable between trials; different starting temperatures (steeper cooling at higher temperature); heat escaping from the top when the lid is omitted"),
    "topics/physics/aqa/P25-black-body-radiation.html": RP(
        "Infrared Radiation from Different Surfaces (AQA RP10 — triple)",
        LI("Fill a Leslie cube (or identical containers) with very hot water; the faces have different surfaces — matt black, gloss black, matt white, shiny metal")
        + LI("Place an infrared detector (or a thermometer with a blackened bulb) at a FIXED distance from one face, level with its centre")
        + LI("Record the detector reading, then repeat at the same distance for every face")
        + LI("Compare readings: the matt black surface emits the most infrared, the shiny metal surface the least")
        + LI("Variables: surface type (independent), amount of infrared detected (dependent), distance, angle and water temperature (controls)"),
        "detector distance or angle changing between faces (readings are very distance-sensitive); parallax when aligning; comparing surfaces at different water temperatures"),
    "topics/combined-science/aqa/C14-electrolysis.html": RP(
        "Electrolysis of Aqueous Solutions (AQA required practical)",
        LI("Set up a beaker with the test solution and two inert electrodes connected to a low-voltage DC supply")
        + LI("Switch on and observe each electrode for bubbles or solid deposits")
        + LI("Test any gases: hydrogen gives a squeaky pop with a burning splint; oxygen relights a glowing splint; chlorine bleaches damp litmus paper")
        + LI("Record the product at the cathode (negative electrode) and the anode (positive electrode)")
        + LI("Repeat with a different solution to compare the products"),
        "electrodes touching; voltage too low; mixing up the cathode (negative) and anode (positive)"),
    "topics/combined-science/aqa/C15-exothermic-and-endothermic-reactions.html": RP(
        "Temperature Changes in Reactions (AQA required practical)",
        LI("Put a fixed volume of dilute acid in a polystyrene cup with a lid and record the starting temperature")
        + LI("Add a measured amount of the second reactant, stir gently and record the maximum or minimum temperature")
        + LI("Calculate the temperature change: a rise means exothermic, a fall means endothermic")
        + LI("Repeat with different concentrations and compare the temperature changes"),
        "no lid (heat loss); reading the thermometer too late; unequal volumes or starting temperatures"),
    "topics/combined-science/aqa/P2-conservation-and-efficiency.html": RP(
        "Thermal Insulation Factors (AQA required practical)",
        LI("Pour a fixed volume of hot water (same starting temperature) into a container")
        + LI("Wrap the container in one insulating material and thickness, with a lid")
        + LI("Record the temperature every minute for 10 minutes")
        + LI("Repeat changing only the insulator or thickness, keeping everything else the same")
        + LI("Compare the cooling curves — the shallowest gradient is the best insulator"),
        "changing two variables at once; different starting temperatures; leaving the lid off"),
    "topics/combined-science/aqa/B20-ecosystems.html": RP(
        "Sampling with Quadrats (AQA required practical)",
        LI("At the study site, mark out a large area and generate random coordinates (from a grid of two random numbers) for placing a quadrat — this avoids bias")
        + LI("At each point, lay the quadrat and count the chosen species (or estimate percentage cover)")
        + LI("Take at least 10 readings and calculate the mean per quadrat, then scale up: mean × (total area ÷ quadrat area)")
        + LI("To study a gradient (e.g. light from woodland edge to open field), use a transect: lay a tape measure and place quadrats at regular intervals along it")
        + LI("Variables: position along the transect (independent), abundance of the species (dependent), quadrat size and season (controls)"),
        "throwing quadrats (biases towards visible plants); too few quadrats (unrepresentative mean); counting only the quadrats where the species is obvious"),
    "topics/biology/aqa/B20-ecosystems.html": RP(
        "Sampling Along a Transect (AQA RP7 — see also B22 for quadrat sampling)",
        LI("Stretch a tape measure across the habitat where an environmental gradient exists (e.g. shaded under a tree to open grassland)")
        + LI("Place a quadrat at regular intervals (e.g. every 2 m) along the tape — a belt transect")
        + LI("At each point, record the abundance of your chosen species (count, or estimate percentage cover) and measure the abiotic factor (e.g. light level with a light meter)")
        + LI("Plot abundance against the abiotic factor to describe how distribution changes along the gradient")
        + LI("Variables: distance along the transect (independent), species abundance (dependent), quadrat size and time of day for light readings (controls)"),
        "light readings taken at different times of day (the confounding variable); irregular quadrat spacing; too few points along the gradient"),
}

if __name__ == "__main__":
    for path, box in JOBS.items():
        html = open(path, encoding="utf-8").read()
        title = box.split('<h3>')[1].split('</h3>')[0]
        if title in html:
            print(f"{path}: SKIP (already present)")
            continue
        html, ok = insert_before_section(html, "🎯 Exam Tips", box)
        print(f"{path}: {'inserted' if ok else 'NO ANCHOR'}")
        if ok:
            open(path, "w", encoding="utf-8").write(html)
