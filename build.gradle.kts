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
