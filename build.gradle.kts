plugins {
    kotlin("jvm") version "2.3.21"
    application
}

repositories {
    mavenCentral()
}

sourceSets {
    main {
        kotlin.srcDir("problems")
    }
}

application {
    mainClass.set(providers.gradleProperty("mainClass"))
}
