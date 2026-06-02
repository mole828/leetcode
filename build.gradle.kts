plugins {
    kotlin("jvm") version "2.3.21"
}

repositories {
    mavenCentral()
}

sourceSets {
    main {
        kotlin.srcDir("problems")
    }
}
