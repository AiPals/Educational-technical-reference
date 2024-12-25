import os
import subprocess

# Define the folder structure
folders = [
    "src/components/visualizers",
    "src/components/tables",
    "src/components/subjects/calculus",
    "src/components/subjects/chemistry",
    "src/components/subjects/physics",
    "src/components/interactive/achievements",
    "src/components/interactive/sound",
    "src/components/ui",
    "src/lib/formulas",
    "src/lib/utils",
    "src/lib/data",
    "src/types",
    "src/styles",
    "src/app/subjects/calculus/[topic]",
    "src/app/subjects/physics",
    "src/app/subjects/chemistry",
    "src/app/interactive",
    "public/images/subjects",
    "public/images/achievements",
    "public/audio/effects",
    "public/audio/celebrations",
    "tests/components",
    "tests/utils",
]

# Define the files to be created
files = [
    "package.json",
    "README.md",
    "tsconfig.json",
    "tailwind.config.js",
    "src/styles/globals.css",
    "src/styles/animations.css",
    "src/app/page.tsx",
    "src/app/subjects/calculus/page.tsx",
    "src/app/subjects/physics/page.tsx",
    "src/app/subjects/chemistry/page.tsx",
    "src/app/interactive/page.tsx",
    "src/components/visualizers/MathVisualization.tsx",
    "src/components/visualizers/CryptoVisualizer.tsx",
    "src/components/visualizers/NetworkProtocolVisualizer.tsx",
    "src/components/visualizers/CalculusVisualizer.tsx",
    "src/components/visualizers/PhysicsSimulator.tsx",
    "src/components/visualizers/ChemistryVisualizer.tsx",
    "src/components/tables/ElementsTable.tsx",
    "src/components/tables/CalculusTopics.tsx",
    "src/components/tables/PhysicsConstants.tsx",
    "src/components/tables/ChemicalReactions.tsx",
    "src/components/subjects/calculus/Calculus1.tsx",
    "src/components/subjects/calculus/Calculus2.tsx",
    "src/components/subjects/chemistry/PeriodicTable.tsx",
    "src/components/subjects/chemistry/Reactions.tsx",
    "src/components/subjects/physics/Mechanics.tsx",
    "src/components/subjects/physics/Thermodynamics.tsx",
    "src/components/interactive/achievements/AchievementSystem.tsx",
    "src/components/interactive/achievements/Celebrations.tsx",
    "src/components/interactive/sound/SoundController.tsx",
    "src/components/interactive/sound/AudioEffects.tsx",
    "src/components/ui/Card.tsx",
    "src/components/ui/Tabs.tsx",
    "src/components/ui/Navigation.tsx",
    "src/lib/formulas/math.ts",
    "src/lib/formulas/crypto.ts",
    "src/lib/formulas/network.ts",
    "src/lib/formulas/calculus.ts",
    "src/lib/formulas/physics.ts",
    "src/lib/formulas/chemistry.ts",
    "src/lib/utils/plotting.ts",
    "src/lib/utils/visualization.ts",
    "src/lib/utils/achievements.ts",
    "src/lib/utils/audio.ts",
    "src/lib/data/subjects.ts",
    "src/lib/data/achievements.ts",
    "src/lib/data/audioEffects.ts",
    "src/types/index.ts",
    "src/types/subjects.ts",
    "src/types/achievements.ts",
    "src/types/audio.ts",
    "tests/components/visualizers.test.tsx",
    "tests/components/subjects.test.tsx",
    "tests/utils/plotting.test.ts",
    "tests/utils/audio.test.ts",
]

# Create the directories
for folder in folders:
    os.makedirs(folder, exist_ok=True)

# Create the files
for file in files:
    with open(file, 'w') as f:
        pass  # Create empty file

# Initialize Git repository if not already done
if not os.path.exists('.git'):
    subprocess.run(['git', 'init'])

# Add all files to Git
subprocess.run(['git', 'add', '.'])

# Commit the changes
subprocess.run(['git', 'commit', '-m', 'Initial commit with folder structure'])

# Push the changes to the remote repository
subprocess.run(['git', 'push', '-u', 'origin', 'main'])