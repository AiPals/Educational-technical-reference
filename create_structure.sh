#!/bin/bash

# Create main directories
mkdir -p src/{components/{visualizers,tables,subjects/{calculus,chemistry,physics},interactive/{achievements,sound},ui},lib/{formulas,utils,data},types,styles,app/{subjects/{calculus/\[topic\],physics,chemistry},interactive},public/{images/{subjects,achievements},audio/{effects,celebrations}},tests/{components,utils}}

# Create main files
touch package.json README.md tsconfig.json tailwind.config.js
touch src/{styles/{globals.css,animations.css},app/{page.tsx,subjects/{calculus/page.tsx,physics/page.tsx,chemistry/page.tsx},interactive/page.tsx}}

# Create component files
touch src/components/visualizers/{MathVisualization.tsx,CryptoVisualizer.tsx,NetworkProtocolVisualizer.tsx,CalculusVisualizer.tsx,PhysicsSimulator.tsx,ChemistryVisualizer.tsx}
touch src/components/tables/{ElementsTable.tsx,CalculusTopics.tsx,PhysicsConstants.tsx,ChemicalReactions.tsx}
touch src/components/subjects/calculus/{Calculus1.tsx,Calculus2.tsx}
touch src/components/subjects/chemistry/{PeriodicTable.tsx,Reactions.tsx}
touch src/components/subjects/physics/{Mechanics.tsx,Thermodynamics.tsx}
touch src/components/interactive/achievements/{AchievementSystem.tsx,Celebrations.tsx}
touch src/components/interactive/sound/{SoundController.tsx,AudioEffects.tsx}
touch src/components/ui/{Card.tsx,Tabs.tsx,Navigation.tsx}

# Create library files
touch src/lib/formulas/{math.ts,crypto.ts,network.ts,calculus.ts,physics.ts,chemistry.ts}
touch src/lib/utils/{plotting.ts,visualization.ts,achievements.ts,audio.ts}
touch src/lib/data/{subjects.ts,achievements.ts,audioEffects.ts}

# Create types files
touch src/types/{index.ts,subjects.ts,achievements.ts,audio.ts}

# Create tests files
touch tests/components/{visualizers.test.tsx,subjects.test.tsx}
touch tests/utils/{plotting.test.ts,audio.test.ts}