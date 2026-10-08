plugins {
    kotlin("jvm") version "2.4.0"
    application
}

repositories {
    mavenCentral()
}

sourceSets {
    main {
        kotlin.srcDir("problems")
        providers.gradleProperty("problemNumber").orNull?.let { problemNumber ->
            kotlin.include("p$problemNumber/Solution.kt")
        }
    }
}

application {
    mainClass.set(providers.gradleProperty("mainClass"))
}

// VS Code registers ideRun through an init script after evaluating this project.
// Wait for that registration, then use its selected main class to scope compilation.
gradle.projectsEvaluated {
    val ideRun = tasks.findByName("ideRun") as? JavaExec
    val problemNumber = ideRun?.mainClass?.orNull
        ?.let { Regex("^p([0-9]+)\\.SolutionKt$").matchEntire(it) }
        ?.groupValues?.get(1)
    if (problemNumber != null && !providers.gradleProperty("problemNumber").isPresent) {
        sourceSets.main {
            kotlin.include("p$problemNumber/Solution.kt")
        }
    }
}
