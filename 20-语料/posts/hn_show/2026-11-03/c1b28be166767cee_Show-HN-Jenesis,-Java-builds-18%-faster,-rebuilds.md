---
type: "corpus"
item_id: "c1b28be166767cee"
title: "Show HN: Jenesis, Java builds 18% faster, rebuilds up to 88% faster"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50340526"
project_url: "https://jenesis.build/why/tool"
author: "raphw"
published_at: "2026-11-02T17:42:25Z"
captured_at: "2026-11-03T09:54:09+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-11-03"
pub_day: "2026-11-02"
tags:
  - 语料
  - hn_show
  - author_raphw
  - story_50340526
  - show_hn
metrics: {"points": 5, "comments": 0, "engagement_velocity": 5}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:3d"
---

# Show HN: Jenesis, Java builds 18% faster, rebuilds up to 88% faster

> [!info] 一句话导读
> Jenesis - you already wrote the build script

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50340526>
> 指标：点赞=5 · 评论=0 · engagement_velocity=5
> 作者：raphw　|　发布：2026-11-02T17:42:25Z
> 项目链接：<https://jenesis.build/why/tool>
> 采集：2026-11-03T09:54:09+08:00　|　id：`c1b28be166767cee`

## 正文

Jenesis - you already wrote the build script

# You already wrote the build script.

 Java builds have grown verbose. A `pom.xml`, a `build.gradle.kts` or a `BUILD.bazel` restates what the code already says - its name, its dependencies, its main class - and grows a block of configuration for every step beyond the defaults, until the build is a second program to maintain beside the first. Jenesis reads the build from the code instead: `module-info.java` names what the project requires, and its Javadoc carries any metadata. There is nothing else to write, and no build tool to download.

 Not moving to modules yet? Jenesis builds the `pom.xml` you already have, on the class path as Maven does, and the speed and the checks come with it: `pin` records the version and SHA-256 checksum of every dependency in a comment of the `pom.xml`, which Maven ignores, and a build that downloads other bytes fails. Every build timed below is built from its `pom.xml`.

 module-info.java pom.xml

```
$ curl -fsSL https://get.jenesis.build | bash
$ cat sources/module-info.java
/**
 * @jenesis.release 25
 * @jenesis.main demo.app.Main
 */
module demo.app {
    requires org.slf4j;
    requires com.fasterxml.jackson.databind;
    requires info.picocli;
    requires static org.jspecify;
}
$ java build/jenesis/Make.java
```

```
$ curl -fsSL https://get.jenesis.build | bash
$ cat pom.xml
<project>
    <modelVersion>4.0.0</modelVersion>
    <groupId>demo</groupId>
    <artifactId>app</artifactId>
    <version>1.0.0</version>
    <dependencies>
        <dependency>
            <groupId>com.fasterxml.jackson.core</groupId>
            <artifactId>jackson-databind</artifactId>
            <version>2.20.0</version>
        </dependency>
    </dependencies>
</project>
$ java build/jenesis/Make.java
```

## At least as fast as the build it replaces.

A coding agent moved eight open-source builds to Jenesis, each from the prompt below and nothing else. Doing the same work as the original build, Jenesis was never slower: across the projects, a full build took a median 15 to 21 % less time, a build after one method was edited about 30 % less, and a build with nothing changed over 90 % less, where Maven runs every test again. Its ahead-of-time mode brings close to a daemon's speed to a CI server, where no process outlives a build, by starting each build from the classes and the JIT's method profiles that earlier builds left in a cache. Jenesis does all this with about 50,000 lines of code and no library, against about 540,000 for Maven 3.9 with the plugins and libraries it downloads to build and publish a jar, and about 3.4 million for the Gradle distribution.

| Project | Built with | Agent time | Full build Jenesis / before | Nothing changed Jenesis / before | One method edited Jenesis / before |
| --- | --- | --- | --- | --- | --- |
| Guava | Maven | 57 min | −15 % 11 min 25 s / 13 min 30 s | −99 % 4 s / 12 min 50 s | −18 % 10 min 40 s / 13 min 5 s |
| JUnit 5 | Gradle | 1 h 18 min | −13 % 3 min 40 s / 4 min 20 s | −62 % 7 s / 18 s | −24 % 2 min 10 s / 2 min 55 s |
| Mockito | Gradle | 53 min | −9 % 3 min 20 s / 3 min 45 s | −73 % 6 s / 23 s | −1 % 2 min 55 s / 2 min 55 s |
| AssertJ | Maven | 45 min | −33 % 95 s / 2 min 20 s | −96 % 4 s / 118 s | −47 % 65 s / 2 min 5 s |
| Google Auto | Maven | 37 min | −19 % 80 s / 99 s | −96 % 4 s / 95 s | −68 % 31 s / 99 s |
| Jackson Databind | Maven | 23 min | −15 % 55 s / 66 s | −93 % 4 s / 67 s | −33 % 44 s / 66 s |
| Gson | Maven | 30 min | −24 % 55 s / 73 s | −91 % 4 s / 44 s | −70 % 20 s / 67 s |
| jsoup | Maven | 32 min | −20 % 41 s / 52 s | −93 % 3 s / 40 s | −8 % 36 s / 40 s |
| Median saving | | | −17 % | −93 % | −29 % |

| Project | Built with | Agent time | Full build Jenesis / before | Nothing changed Jenesis / before | One method edited Jenesis / before |
| --- | --- | --- | --- | --- | --- |
| Guava | Maven | 57 min | −15 % 10 min 45 s / 12 min 40 s | −99 % 3 s / 12 min 20 s | −18 % 10 min 20 s / 12 min 40 s |
| JUnit 5 | Gradle | 1 h 18 min | −32 % 2 min 40 s / 3 min 55 s | −38 % 4 s / 7 s | −39 % 104 s / 2 min 50 s |
| Mockito | Gradle | 53 min | −16 % 2 min 40 s / 3 min 10 s | −46 % 4 s / 7 s | −6 % 2 min 25 s / 2 min 35 s |
| AssertJ | Maven | 45 min | −32 % 70 s / 103 s | −96 % 3 s / 80 s | −33 % 59 s / 88 s |
| Google Auto | Maven | 37 min | 0 % 72 s / 72 s | −97 % 2 s / 70 s | −71 % 20 s / 70 s |
| Jackson Databind | Maven | 23 min | −8 % 49 s / 53 s | −96 % 2 s / 54 s | −30 % 36 s / 52 s |
| Gson | Maven | 30 min | −32 % 33 s / 49 s | −90 % 2 s / 22 s | −68 % 14 s / 43 s |
| jsoup | Maven | 32 min | −6 % 35 s / 38 s | −94 % 2 s / 31 s | −1 % 31 s / 31 s |
| Median saving | | | −15 % | −95 % | −32 % |

| Project | Built with | Agent time | Full build Jenesis / before | Nothing changed Jenesis / before | One method edited Jenesis / before |
| --- | --- | --- | --- | --- | --- |
| Guava | Maven | 57 min | −17 % 11 min 10 s / 13 min 30 s | −99 % 2 s / 12 min 50 s | −19 % 10 min 30 s / 13 min 5 s |
| JUnit 5 | Gradle | 1 h 18 min | −20 % 3 min 25 s / 4 min 20 s | −69 % 5 s / 18 s | −25 % 2 min 10 s / 2 min 55 s |
| Mockito | Gradle | 53 min | −10 % 3 min 20 s / 3 min 45 s | −80 % 5 s / 23 s | −1 % 2 min 55 s / 2 min 55 s |
| AssertJ | Maven | 45 min | −34 % 93 s / 2 min 20 s | −97 % 3 s / 118 s | −47 % 66 s / 2 min 5 s |
| Google Auto | Maven | 37 min | −16 % 83 s / 99 s | −97 % 2 s / 95 s | −73 % 27 s / 99 s |
| Jackson Databind | Maven | 23 min | −22 % 51 s / 66 s | −96 % 3 s / 67 s | −36 % 42 s / 66 s |
| Gson | Maven | 30 min | −39 % 45 s / 73 s | −96 % 2 s / 44 s | −76 % 16 s / 67 s |
| jsoup | Maven | 32 min | −26 % 38 s / 52 s | −96 % 1 s / 40 s | −18 % 32 s / 40 s |
| Median saving | | | −21 % | −96 % | −30 % |

Each build ran alone on a four-core machine, and a time is the median of three runs. Without a daemon, Maven ran as `mvn` and Gradle with `--no-daemon`; with one, Jenesis' daemon ran against `mvnd` and Gradle's, each warmed up by a first build. From an ahead-of-time cache, Jenesis is set beside the original build without a daemon, as on a CI server, where a daemon often does not outlive a build but a cache kept in a file does. Every build stayed on `pom.xml` and ran the same tests, apart from the few Jenesis leaves to the old build. One machine and a few runs make this imperfect, but the tendency holds for every project. Lines of code are counted without comments or blank lines.

 Each migration's patch and the script that timed it, to run on your own machine →

## Hand the move to a coding agent.

Hand it this prompt, or start one with it from the root of the project.

 Prompt `Run `curl -fsSL https://get.jenesis.build | bash` in the root of this project, then run `java build/jenesis/Make.java prompt/migrate` and carry out the task it prints.` Copy

 Claude Code `claude 'Run `curl -fsSL https://get.jenesis.build | bash` in the root of this project, then run `java build/jenesis/Make.java prompt/migrate` and carry out the task it prints.'` Copy

 Codex `codex 'Run `curl -fsSL https://get.jenesis.build | bash` in the root of this project, then run `java build/jenesis/Make.java prompt/migrate` and carry out the task it prints.'` Copy

## Fourteen common builds, in four tools.

 Each section below is one build need, written for Jenesis, Maven, Gradle and Bazel. Every file shown was built and run with that tool. Where a tool needs a plugin, code by hand, or cannot do it at all, the section says so - Jenesis included.

 Built and run on Java 25 with Jenesis 0.18.0, Maven 3.9.16, Gradle 9.8.0 and Bazel 9.2.0.

## Hello, world

One class that prints a line, and nothing else. Before any feature comes into play, it shows what each tool asks for: the files you write, where the source goes, and how the build tool itself ships with the repository.

Jenesis reads the Java Module System's own descriptor, `module-info.java`, where two Javadoc tags name the Java release and the main class. The other tools each bring a build file of their own.

- Jenesis Source Embedded in the repository as source: `build/jenesis/`, a 0.6 MB download as a sources jar or a git submodule. A clean build downloads nothing more.
- Maven Download The Maven Wrapper downloads a 9.4 MB binary release, and a clean build then 20 MB of plugins: 30 MB in total.
- Gradle Download The Gradle Wrapper, a 47 KB jar in the repository, downloads a 152 MB binary release, and this build needs no plugin beyond it: 152 MB in total.
- Bazel Not possible The repository cannot bootstrap Bazel: every machine installs Bazelisk first, 7 MB, which downloads the 66 MB Bazel binary `.bazelversion` names. A clean build then downloads 131 MB: 204 MB in total.

`sources/module-info.java` 6 lines

```
/** * @jenesis.release 25 * @jenesis.main demo.hello.Main */module demo.hello {}
```

`sources/demo/hello/Main.java` 8 lines

```
package demo.hello;public class Main {    public static void main(String[] args) {        System.out.println("Hello, world!");    }}
```

`Terminal`

```
$ java build/jenesis/Execute.java[COMPLETED] Finished in 0.44 secondsHello, world!
```

Worth knowing

- The first run compiles `build/jenesis/` into `.jenesis/` once, as Maven and Gradle download their release on first use; later runs start from those classes.
- The last section installs `build/jenesis/`. The terminal shows the build's last line.

`pom.xml` 11 lines

```
<project xmlns="http://maven.apache.org/POM/4.0.0">  <modelVersion>4.0.0</modelVersion>  <groupId>demo</groupId>  <artifactId>hello</artifactId>  <version>1.0.0</version>  <properties>    <maven.compiler.release>25</maven.compiler.release>    <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>  </properties></project>
```

`.mvn/wrapper/maven-wrapper.properties` written by `mvn wrapper:wrapper` · 3 lines

```
wrapperVersion=3.3.4distributionType=only-scriptdistributionUrl=https://repo.maven.apache.org/maven2/org/apache/maven/apache-maven/3.9.16/apache-maven-3.9.16-bin.zip
```

`src/main/java/demo/hello/Main.java` 8 lines

```
package demo.hello;public class Main {    public static void main(String[] args) {        System.out.println("Hello, world!");    }}
```

`Terminal`

```
$ ./mvnw package[INFO] BUILD SUCCESS$ java -cp target/hello-1.0.0.jar demo.hello.MainHello, world!
```

`build.gradle.kts` 11 lines

```
plugins {    application}java {    toolchain.languageVersion = JavaLanguageVersion.of(25)}application {    mainClass = "demo.hello.Main"}
```

`settings.gradle.kts` 1 line

```
rootProject.name = "hello"
```

`gradle/wrapper/gradle-wrapper.properties` written by `gradle wrapper` · 10 lines

```
distributionBase=GRADLE_USER_HOMEdistributionPath=wrapper/distsdistributionSha256Sum=bafd5ce9cfaea0fbccfdc8439a1ac42fbd4cd9c89dc9a988228d8a2639a58e6cdistributionUrl=https\://services.gradle.org/distributions/gradle-9.8.0-bin.zipnetworkTimeout=10000retries=0retryBackOffMs=500validateDistributionUrl=truezipStoreBase=GRADLE_USER_HOMEzipStorePath=wrapper/dists
```

`src/main/java/demo/hello/Main.java` 8 lines

```
package demo.hello;public class Main {    public static void main(String[] args) {        System.out.println("Hello, world!");    }}
```

`Terminal`

```
$ ./gradlew run> Task :runHello, world!BUILD SUCCESSFUL in 5s
```

`MODULE.bazel` 3 lines

```
module(name = "hello", version = "1.0.0")bazel_dep(name = "rules_java", version = "9.9.0")
```

`BUILD.bazel` 15 lines

```
load("@rules_java//java:java_binary.bzl", "java_binary")load("@rules_java//toolchains:default_java_toolchain.bzl", "default_java_toolchain")java_binary(    name = "hello",    srcs = glob(["src/main/java/**/*.java"]),    main_class = "demo.hello.Main",)default_java_toolchain(    name = "local_toolchain",    java_runtime = "@rules_java//toolchains:current_host_java_runtime",    source_version = "25",    target_version = "25",)
```

Without the toolchain, rules_java downloads a JDK 25 of its own to compile with.

`.bazelrc` 5 lines

```
common --java_language_version=25common --java_runtime_version=local_jdkcommon --tool_java_language_version=25common --tool_java_runtime_version=local_jdkcommon --extra_toolchains=//:local_toolchain_definition
```

Without it rules_java compiles for Java 11 and downloads its own JDKs.

`.bazelversion` 1 line

```
9.2.0
```

`MODULE.bazel.lock` written by `Bazel, on every build` · 456 lines

`src/main/java/demo/hello/Main.java` 8 lines

```
package demo.hello;public class Main {    public static void main(String[] args) {        System.out.println("Hello, world!");    }}
```

`Terminal`

```
$ bazel run //:helloINFO: Build completed successfully, 9 total actionsHello, world!
```

## A modular build in Java

A Java 25 application with four dependencies, written as a module. Its `module-info.java` is the Java Module System's own descriptor: it names what the module reads, and `javac` compiles and checks it. Jenesis takes it as the build. Its `requires` are the dependencies, two Javadoc tags set the release and the main class, and versions are optional pins in the same file.

The other tools compile the same descriptor, but each dependency must be declared again in their own format - highlighted in their tabs.

- Jenesis Built in The module descriptor is the build file.
- Maven Declared twice Every `requires` again as a ` `.
- Gradle Declared twice Every `requires` again as `implementation(...)`.
- Bazel Declared three times Every `requires` again as a coordinate and as a label. It runs on the class path.

`sources/module-info.java` 14 lines

```
/** * @jenesis.release 25 * @jenesis.main demo.app.Main * @jenesis.pin org.slf4j 2.0.20 * @jenesis.pin com.fasterxml.jackson.databind 2.22.3 * @jenesis.pin info.picocli 4.7.7 * @jenesis.pin org.jspecify 1.0.1 */module demo.app {    requires org.slf4j;    requires com.fasterxml.jackson.databind;    requires info.picocli;    requires static org.jspecify;}
```

`src/main/java/module-info.java` 6 lines

```
module demo.app {    requires org.slf4j;    requires com.fasterxml.jackson.databind;    requires info.picocli;    requires static org.jspecify;}
```

`pom.xml` 47 lines

```
<project xmlns="http://maven.apache.org/POM/4.0.0">  <modelVersion>4.0.0</modelVersion>  <groupId>demo</groupId>  <artifactId>app</artifactId>  <version>1.0.0</version>  <properties>    <maven.compiler.release>25</maven.compiler.release>    <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>  </properties>  <dependencies>    <dependency>      <groupId>org.slf4j</groupId>      <artifactId>slf4j-api</artifactId>      <version>2.0.20</version>    </dependency>    <dependency>      <groupId>com.fasterxml.jackson.core</groupId>      <artifactId>jackson-databind</artifactId>      <version>2.22.3</version>    </dependency>    <dependency>      <groupId>info.picocli</groupId>      <artifactId>picocli</artifactId>      <version>4.7.7</version>    </dependency>    <dependency>      <groupId>org.jspecify</groupId>      <artifactId>jspecify</artifactId>      <version>1.0.1</version>    </dependency>  </dependencies>  <build>    <plugins>      <plugin>        <artifactId>maven-compiler-plugin</artifactId>        <version>3.16.0</version>      </plugin>      <plugin>        <artifactId>maven-jar-plugin</artifactId>        <version>3.5.1</version>      </plugin>    </plugins>  </build></project>
```

- A third-party extension derives them from `requires`, but the published POM then lists no dependencies.

`src/main/java/module-info.java` 6 lines

```
module demo.app {    requires org.slf4j;    requires com.fasterxml.jackson.databind;    requires info.picocli;    requires static org.jspecify;}
```

`build.gradle.kts` 26 lines

```
plugins {    application}group = "demo"version = "1.0.0"java {    toolchain.languageVersion = JavaLanguageVersion.of(25)}repositories {    mavenCentral()}dependencies {    implementation("org.slf4j:slf4j-api:2.0.20")    implementation("com.fasterxml.jackson.core:jackson-databind:2.22.3")    implementation("info.picocli:picocli:4.7.7")    implementation("org.jspecify:jspecify:1.0.1")}application {    mainModule = "demo.app"    mainClass = "demo.app.Main"}
```

`settings.gradle.kts` 1 line

```
rootProject.name = "app"
```

`gradle/wrapper/gradle-wrapper.properties` written by `gradle wrapper` · 10 lines

```
distributionBase=GRADLE_USER_HOMEdistributionPath=wrapper/distsdistributionSha256Sum=bafd5ce9cfaea0fbccfdc8439a1ac42fbd4cd9c89dc9a988228d8a2639a58e6cdistributionUrl=https\://services.gradle.org/distributions/gradle-9.8.0-bin.zipnetworkTimeout=10000retries=0retryBackOffMs=500validateDistributionUrl=truezipStoreBase=GRADLE_USER_HOMEzipStorePath=wrapper/dists
```

- GradleX's third-party plugin derives them from `requires`; the versions then go into a version catalog.

`src/main/java/module-info.java` 6 lines

```
module demo.app {    requires org.slf4j;    requires com.fasterxml.jackson.databind;    requires info.picocli;    requires static org.jspecify;}
```

`MODULE.bazel` 16 lines

```
module(name = "app", version = "1.0.0")bazel_dep(name = "rules_java", version = "9.9.0")bazel_dep(name = "rules_jvm_external", version = "7.1")maven = use_extension("@rules_jvm_external//:extensions.bzl", "maven")maven.install(    artifacts = [        "org.slf4j:slf4j-api:2.0.20",        "com.fasterxml.jackson.core:jackson-databind:2.22.3",        "info.picocli:picocli:4.7.7",        "org.jspecify:jspecify:1.0.1",    ],    repositories = ["https://repo1.maven.org/maven2"],)use_repo(maven, "maven")
```

`BUILD.bazel` 13 lines

```
load("@rules_java//java:java_binary.bzl", "java_binary")java_binary(    name = "app",    srcs = glob(["src/main/java/**/*.java"]),    main_class = "demo.app.Main",    deps = [        "@maven//:org_slf4j_slf4j_api",        "@maven//:com_fasterxml_jackson_core_jackson_databind",        "@maven//:info_picocli_picocli",        "@maven//:org_jspecify_jspecify",    ],)
```

`.bazelrc` 2 lines

```
common --java_language_version=25common --java_runtime_version=remotejdk_25
```

Without it rules_java compiles for Java 11.

`.bazelversion` 1 line

```
9.2.0
```

`MODULE.bazel.lock` written by `Bazel, on every build` · 814 lines

## Tests with JUnit 6

A Jenesis test is a module of its own. It names the module it tests and requires the JUnit API; the engine and the console runner follow from that, so neither is declared. The module under test lets the tests in with a qualified export - `exports demo.app to demo.app.test` - and no other module can read the package.

- Jenesis Built in A test module that names the module it tests. The engine is inferred.
- Maven Built in One test dependency. Surefire runs JUnit 6 unchanged.
- Gradle Built in `useJUnitPlatform()` and an explicit launcher dependency.
- Bazel Community ruleset `java_test` runs JUnit 4 only. JUnit 6 takes `java_junit5_test` from contrib_rules_jvm.

`tests/module-info.java` 8 lines

```
/** * @jenesis.test demo.app * @jenesis.pin org.junit.jupiter.api 6.1.3 */module demo.app.test {    requires demo.app;    requires org.junit.jupiter.api;}
```

`sources/module-info.java` 16 lines

```
/** * @jenesis.release 25 * @jenesis.main demo.app.Main * @jenesis.pin org.slf4j 2.0.20 * @jenesis.pin com.fasterxml.jackson.databind 2.22.3 * @jenesis.pin info.picocli 4.7.7 * @jenesis.pin org.jspecify 1.0.1 */module demo.app {    requires org.slf4j;    requires com.fasterxml.jackson.databind;    requires info.picocli;    requires static org.jspecify;    exports demo.app to demo.app.test;}
```

Worth knowing

- Tests see what the module under test exports to them, and nothing else.

`pom.xml` 57 lines

```
<project xmlns="http://maven.apache.org/POM/4.0.0">  <modelVersion>4.0.0</modelVersion>  <groupId>demo</groupId>  <artifactId>app</artifactId>  <version>1.0.0</version>  <properties>    <maven.compiler.release>25</maven.compiler.release>    <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>  </properties>  <dependencies>    <dependency>      <groupId>org.slf4j</groupId>      <artifactId>slf4j-api</artifactId>      <version>2.0.20</version>    </dependency>    <dependency>      <groupId>com.fasterxml.jackson.core</groupId>      <artifactId>jackson-databind</artifactId>      <version>2.22.3</version>    </dependency>    <dependency>      <groupId>info.picocli</groupId>      <artifactId>picocli</artifactId>      <version>4.7.7</version>    </dependency>    <dependency>      <groupId>org.jspecify</groupId>      <artifactId>jspecify</artifactId>      <version>1.0.1</version>    </dependency>    <dependency>      <groupId>org.junit.jupiter</groupId>      <artifactId>junit-jupiter</artifactId>      <version>6.1.3</version>      <scope>test</scope>    </dependency>  </dependencies>  <build>    <plugins>      <plugin>        <artifactId>maven-compiler-plugin</artifactId>        <version>3.16.0</version>      </plugin>      <plugin>        <artifactId>maven-surefire-plugin</artifactId>        <version>3.6.0</version>      </plugin>      <plugin>        <artifactId>maven-jar-plugin</artifactId>        <version>3.5.1</version>      </plugin>    </plugins>  </build></project>
```

Worth knowing

- Tests live in the same package, compiled on top of the main classes.

`build.gradle.kts` 28 lines

```
plugins {    java}group = "demo"version = "1.0.0"java {    toolchain.languageVersion = JavaLanguageVersion.of(25)}repositories {    mavenCentral()}dependencies {    implementation("org.slf4j:slf4j-api:2.0.20")    implementation("com.fasterxml.jackson.core:jackson-databind:2.22.3")    implementation("info.picocli:picocli:4.7.7")    implementation("org.jspecify:jspecify:1.0.1")    testImplementation("org.junit.jupiter:junit-jupiter:6.1.3")    testRuntimeOnly("org.junit.platform:junit-platform-launcher")}tasks.test {    useJUnitPlatform()}
```

Worth knowing

- Without `junit-platform-launcher` on the test runtime path, Gradle 9 cannot start the JUnit Platform.

`MODULE.bazel` 21 lines

```
module(name = "app", version = "1.0.0")bazel_dep(name = "rules_java", version = "9.9.0")bazel_dep(name = "rules_jvm_external", version = "7.1")bazel_dep(name = "contrib_rules_jvm", version = "0.34.0")maven = use_extension("@rules_jvm_external//:extensions.bzl", "maven")maven.install(    artifacts = [        "org.slf4j:slf4j-api:2.0.20",        "com.fasterxml.jackson.core:jackson-databind:2.22.3",        "info.picocli:picocli:4.7.7",        "org.jspecify:jspecify:1.0.1",        "org.junit.jupiter:junit-jupiter-api:6.1.3",        "org.junit.jupiter:junit-jupiter-engine:6.1.3",        "org.junit.platform:junit-platform-launcher:6.1.3",        "org.junit.platform:junit-platform-reporting:6.1.3",    ],    repositories = ["https://repo1.maven.org/maven2"],)use_repo(maven, "maven")
```

`BUILD.bazel` 31 lines

```
load("@contrib_rules_jvm//java:defs.bzl", "JUNIT5_DEPS", "java_junit5_test")load("@rules_java//java:java_binary.bzl", "java_binary")load("@rules_java//java:java_library.bzl", "java_library")java_library(    name = "lib",    srcs = glob(["src/main/java/**/*.java"]),    deps = [        "@maven//:org_slf4j_slf4j_api",        "@maven//:com_fasterxml_jackson_core_jackson_databind",        "@maven//:info_picocli_picocli",        "@maven//:org_jspecify_jspecify",    ],)java_binary(    name = "app",    main_class = "demo.app.Main",    runtime_deps = [":lib"],)java_junit5_test(    name = "GreeterTest",    srcs = ["src/test/java/demo/app/GreeterTest.java"],    test_class = "demo.app.GreeterTest",    deps = [        ":lib",        "@maven//:org_junit_jupiter_junit_jupiter_api",    ],    runtime_deps = JUNIT5_DEPS,)
```

Worth knowing

- A plain `java_test` with a Jupiter class fails with No runnable methods.
- Every JUnit artifact the runner needs is listed by hand in `MODULE.bazel`.

### Why not test package-private code from the same package?

 Package-private access is for classes that are written and changed together - the collaborators inside one package. A test that sits in that package and calls into it depends on those internals, and nothing declares the dependency: the build never records that the tests read the implementation. A refactoring that keeps the public behaviour can still break them.

 The Java Module System cannot express the arrangement at all. A package belongs to exactly one module, so a test in the same package cannot be a module of its own. It can only be compiled into the module under test with `--patch-module`, and then what runs is no longer what the module descriptor describes. A qualified export states the dependency instead, in the file that already describes the module.

### Maven 4 invents a second descriptor

 Maven 4 and its 4.x compiler plugin compile same-package tests into the module under test. What the tests need beyond the module's own descriptor goes into a new file, `module-info-patch.maven`, in a syntax only Maven reads, with Maven-only keywords such as `TEST-MODULE-PATH`. The compiler honours it; Surefire does not, so what the test run needs is repeated as JVM arguments in `argLine`.

`src/test/java/module-info-patch.maven` a test that also uses java.net.http

```
patch-module demo.app {    add-modules TEST-MODULE-PATH, java.net.http;    add-reads TEST-MODULE-PATH, java.net.http;}
```

### Testing with the Java Module System

| | Tests as their own module | Tests inside the module |
| --- | --- | --- |
| Jenesis | Built in A test module names the module it tests. | Not offered A package belongs to one module. |
| Maven 3.9 | Built in A `module-info.java` in the test sources; Surefire runs it as a named module. | Built in Same-package tests run on the module path. |
| Maven 4 | Deprecated Still runs, with a warning to use `module-info-patch.maven` - which patches the main module instead. | Patch file `module-info-patch.maven` for compiling, `argLine` for running. |
| Gradle 9.8 | Built in A `module-info.java` in the test sources. | By hand A second copy of the main descriptor and `--patch-module` arguments, or the GradleX plugin. By default tests run on the class path. |
| Bazel 9.2 | Class path It compiles as a module, but runs unnamed. | Class path Nothing is ever put on a module path at run time. |

## Only what changed runs again

A build runs after every edit - in watch mode, in continuous integration, and in the loop of a coding agent, which changes a file, builds, reads the result and goes again. That loop is only as fast as the build's answer. Jenesis hashes what each step reads and skips a step whose inputs did not change, the test step included.

One line in `jenesis.properties` keeps every step's result in a cache on the file system, outside `target/`, so a wiped build folder or an edit that is undone costs nothing. One more runs only the tests that reach a changed class. Below is the project of the section before, with the same edits made in every tool.

- Jenesis Built in A step with unchanged inputs is skipped. A cache on disk is one line, test selection another.
- Maven Whole modules Only whole modules. The tests run on every build; Apache's build cache extension restores a module whole or rebuilds it whole, all of its tests included.
- Gradle Whole test tasks The whole test task: one changed class reruns every test of the module. Unchanged tasks are skipped, and one property adds a local build cache.
- Bazel Whole test targets Whole test targets: a changed dependency reruns every test in each target that declares it. Actions are cached by their inputs, and a disk cache is one line.

 Jenesis Maven Gradle Bazel

`jenesis.properties` 2 lines

```
jenesis.project.cachejenesis.test.mode=incremental
```

`Terminal`

```
$ java build/jenesis/Make.javatests >>>>       └─ greets() ✔[COMPLETED] Finished in 2.59 seconds$ java build/jenesis/Make.java    # nothing changed[COMPLETED] Finished in 0.17 seconds$ java build/jenesis/Make.java    # Main.java edited[COMPLETED] Finished in 1.37 seconds$ java build/jenesis/Make.java    # Greeter.java editedtests >>>>       └─ greets() ✔[COMPLETED] Finished in 1.99 seconds$ rm -rf target$ java build/jenesis/Make.java[COMPLETED] Finished in 0.35 seconds
```

Worth knowing

- `GreeterTest` reaches `Greeter` but not `Main`. The terminal shows the test each build ran and its last line; `-Djenesis.print.tests=true` prints the tests.
- Named without a value, `jenesis.project.cache` keeps the cache in `.jenesis/cache`. `jenesis.cache.uri=file:///...` shares one folder between checkouts, and an `https://` address a cache server, such as Jenesis Repository.
- Test selection reads the compiled classes: a test runs when a class it reaches changed. It cannot see reflection, so continuous integration runs the whole suite.

`.mvn/extensions.xml` 7 lines

```
<extensions>  <extension>    <groupId>org.apache.maven.extensions</groupId>    <artifactId>maven-build-cache-extension</artifactId>    <version>1.3.0</version>  </extension></extensions>
```

`Commands`

```
$ mvn verify
```

Worth knowing

- One changed class rebuilds its entire module with the extension and reruns every test in it, whether or not a test reaches the change.
- Without the extension, a build with nothing changed skips the compiler but runs the tests again; one edited class recompiles the main and the test sources; `mvn clean` starts from nothing.

`gradle.properties` 1 line

```
org.gradle.caching=true
```

`Commands`

```
$ ./gradlew build
```

Worth knowing

- After editing `Main.java`, `compileJava` and `test` ran again, `GreeterTest` included; after `clean`, both came `FROM-CACHE` out of `~/.gradle/caches/build-cache-1`.
- Running only the tests a change reaches is part of a commercial offering.

`.bazelrc` 3 lines

```
common --java_language_version=25common --java_runtime_version=remotejdk_25common --disk_cache=~/.cache/bazel-disk
```

`Commands`

```
$ bazel test //...
```

Worth knowing

- `Main.java` shares a target with `Greeter.java`, so editing it reran `GreeterTest`, which never reaches `Main`. Finer selection means one test target per class and small production targets, split by hand.
- After `bazel clean`, 72 of 92 actions came from the disk cache and the test was reported `(cached)`.

### Why the loop matters

 A coding agent works in rounds: it edits, builds, reads what failed and edits again, often many times for one task. Every round waits for the build, so work the build repeats is paid on every round, and a test suite that runs whole after each edit is paid in full each time. A build that answers from what it already knows keeps each round short, and the agent checks more of its work in the same time. The same holds for a developer in watch mode.

### Maven keeps nothing outside `target/`

 Maven asks each plugin whether there is work. The compiler plugin checks its sources and skips an unchanged module; Maven's test plugin has no such check, so the tests run on every build. There is no cache beside the build folder, so `mvn clean` discards everything built so far. Apache's build cache extension adds that cache, but only with the module as its unit: a module is restored whole or rebuilt whole. One changed line in a large module costs that module's full compile and its full test suite, every time.

### What ran again

| | Nothing changed | A class no test reaches | Build folder wiped | An edit undone |
| --- | --- | --- | --- | --- |
| Jenesis | Nothing | Compile, no test | Nothing: cached | Nothing: cached |
| Maven 3.9* | Nothing | The whole module, all tests | Nothing: cached | Nothing: cached |
| Gradle 9.8 | Nothing | Compile, all tests | Nothing: cached | Nothing: cached |
| Bazel 9.2 | Nothing | Compile, all tests | Nothing: cached | Nothing: cached |

* With Apache's build cache extension, which Maven downloads as a plugin. Without it, the tests run on every build and a wiped build folder rebuilds everything.

## Several modules, one build

A library and the application that uses it, built together. In Jenesis the Java module name is how one module of the project refers to another: `requires demo.greeter` is all the wiring there is, and the sibling is built first and resolved from the build itself. There is no root file.

The other tools know a module by a name of their own - an artifact ID, a project path, a label - so each sibling is named twice, and the two names are kept in step by hand. The second one is highlighted in their tabs.

- Jenesis Built in The module name is the reference. No root file.
- Maven Named twice `requires demo.greeter`, and again as the artifact ID `greeter`.
- Gradle Named twice `requires demo.greeter`, and again as the project `:greeter`.
- Bazel Named twice `requires demo.greeter`, and again as the label `//greeter`.

 Jenesis Maven Gradle Bazel

`greeter/module-info.java` 3 lines

```
module demo.greeter {    exports demo.greeter;}
```

`app/module-info.java` 8 lines

```
/** * @jenesis.main demo.app.Main * @jenesis.pin org.slf4j 2.0.20 */module demo.app {    requires demo.greeter;    requires org.slf4j;}
```

`app/src/main/java/module-info.java` 4 lines

```
module demo.app {    requires demo.greeter;    requires org.slf4j;}
```

`app/pom.xml` 22 lines

```
<project xmlns="http://maven.apache.org/POM/4.0.0">  <modelVersion>4.0.0</modelVersion>  <parent>    <groupId>demo</groupId>    <artifactId>parent</artifactId>    <version>1.0.0</version>  </parent>  <artifactId>app</artifactId>  <dependencies>    <dependency>      <groupId>demo</groupId>      <artifactId>greeter</artifactId>      <version>${project.version}</version>    </dependency>    <dependency>      <groupId>org.slf4j</groupId>      <artifactId>slf4j-api</artifactId>      <version>2.0.20</version>    </dependency>  </dependencies></project>
```

`greeter/src/main/java/module-info.java` 3 lines

```
module demo.greeter {    exports demo.greeter;}
```

`greeter/pom.xml` 9 lines

```
<project xmlns="http://maven.apache.org/POM/4.0.0">  <modelVersion>4.0.0</modelVersion>  <parent>    <groupId>demo</groupId>    <artifactId>parent</artifactId>    <version>1.0.0</version>  </parent>  <artifactId>greeter</artifactId></project>
```

`pom.xml` 32 lines

```
<project xmlns="http://maven.apache.org/POM/4.0.0">  <modelVersion>4.0.0</modelVersion>  <groupId>demo</groupId>  <artifactId>parent</artifactId>  <version>1.0.0</version>  <packaging>pom</packaging>  <modules>    <module>greeter</module>    <module>app</module>  </modules>  <properties>    <maven.compiler.release>25</maven.compiler.release>    <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>  </properties>  <build>    <pluginManagement>      <plugins>        <plugin>          <artifactId>maven-compiler-plugin</artifactId>          <version>3.16.0</version>        </plugin>        <plugin>          <artifactId>maven-jar-plugin</artifactId>          <version>3.5.1</version>        </plugin>      </plugins>    </pluginManagement>  </build></project>
```

`app/src/main/java/module-info.java` 4 lines

```
module demo.app {    requires demo.greeter;    requires org.slf4j;}
```

`app/build.gradle.kts` 12 lines

```
plugins {    java}java {    toolchain.languageVersion = JavaLanguageVersion.of(25)}dependencies {    implementation(project(":greeter"))    implementation("org.slf4j:slf4j-api:2.0.20")}
```

`greeter/src/main/java/module-info.java` 3 lines

```
module demo.greeter {    exports demo.greeter;}
```

`greeter/build.gradle.kts` 7 lines

```
plugins {    `java-library`}java {    toolchain.languageVersion = JavaLanguageVersion.of(25)}
```

`settings.gradle.kts` 9 lines

```
rootProject.name = "demo"include("greeter", "app")dependencyResolutionManagement {    repositories {        mavenCentral()    }}
```

`gradle.properties` 2 lines

```
group=demoversion=1.0.0
```

Worth knowing

- Applied in the settings instead, GradleX's third-party plugin finds the project from `requires demo.greeter` by reading its descriptor.

`app/src/main/java/module-info.java` 4 lines

```
module demo.app {    requires demo.greeter;    requires org.slf4j;}
```

`app/BUILD.bazel` 11 lines

```
load("@rules_java//java:java_binary.bzl", "java_binary")java_binary(    name = "app",    srcs = glob(["src/main/java/**/*.java"]),    main_class = "demo.app.Main",    deps = [        "//greeter",        "@maven//:org_slf4j_slf4j_api",    ],)
```

`greeter/src/main/java/module-info.java` 3 lines

```
module demo.greeter {    exports demo.greeter;}
```

`greeter/BUILD.bazel` 7 lines

```
load("@rules_java//java:java_library.bzl", "java_library")java_library(    name = "greeter",    srcs = glob(["src/main/java/**/*.java"]),    visibility = ["//app:__pkg__"],)
```

`MODULE.bazel` 13 lines

```
module(name = "app", version = "1.0.0")bazel_dep(name = "rules_java", version = "9.9.0")bazel_dep(name = "rules_jvm_external", version = "7.1")maven = use_extension("@rules_jvm_external//:extensions.bzl", "maven")maven.install(    artifacts = [        "org.slf4j:slf4j-api:2.0.20",    ],    repositories = ["https://repo1.maven.org/maven2"],)use_repo(maven, "maven")
```

## One jar for Java 21 and Java 25

A multi-release jar carries a Java 21 baseline and, for one class, a second implementation that only a Java 25 runtime loads. With Jenesis the additional sources go where they end up in the jar, under `META-INF/versions/25/`; the build compiles them for 25 in a second pass and marks the manifest.

- Jenesis Built in Sources under `META-INF/versions/25/` are the whole configuration.
- Maven Built in Built in, but configured: a second compiler execution and the manifest entry.
- Gradle By hand No built-in support: a source set and the jar layout by hand.
- Bazel By hand No rule builds one: a genrule unpacks two jars and packs them again.

`sources/module-info.java` 6 lines

```
/** * @jenesis.release 21 * @jenesis.main demo.app.Main */module demo.app {}
```

`Where the sources go`

```
sources/├── module-info.java├── demo/app/Main.java├── demo/app/Platform.java                        compiled for Java 21└── META-INF/versions/25/demo/app/Platform.java   compiled for Java 25
```

`pom.xml` 46 lines

```
<project xmlns="http://maven.apache.org/POM/4.0.0">  <modelVersion>4.0.0</modelVersion>  <groupId>demo</groupId>  <artifactId>app</artifactId>  <version>1.0.0</version>  <properties>    <maven.compiler.release>21</maven.compiler.release>    <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>  </properties>  <build>    <plugins>      <plugin>        <artifactId>maven-compiler-plugin</artifactId>        <version>3.16.0</version>        <executions>          <execution>            <id>java25</id>            <goals>              <goal>compile</goal>            </goals>            <configuration>              <release>25</release>              <compileSourceRoots>                <compileSourceRoot>${project.basedir}/src/main/java25</compileSourceRoot>              </compileSourceRoots>              <multiReleaseOutput>true</multiReleaseOutput>            </configuration>          </execution>        </executions>      </plugin>      <plugin>        <artifactId>maven-jar-plugin</artifactId>        <version>3.5.1</version>        <configuration>          <archive>            <manifestEntries>              <Multi-Release>true</Multi-Release>            </manifestEntries>          </archive>        </configuration>      </plugin>    </plugins>  </build></project>
```

Worth knowing

- The Java 25 sources sit in `src/main/java25`, a folder the second execution names.

`build.gradle.kts` 23 lines

```
plugins {    java}group = "demo"version = "1.0.0"java {    toolchain.languageVersion = JavaLanguageVersion.of(25)}val java25 = sourceSets.create("java25")tasks.compileJava {    options.release = 21}tasks.jar {    into("META-INF/versions/25") {        from(java25.output)    }    manifest.attributes("Multi-Release" to true)}
```

Worth knowing

- The long-used `val java25 by sourceSets.creating` is deprecated in Gradle 9.8.

`BUILD.bazel` 28 lines

```
load("@rules_java//java:java_library.bzl", "java_library")java_library(    name = "base",    srcs = glob(["src/main/java/

## 关联链接

- http://maven.apache.org/POM/4.0.0
- https://`
- https://get.jenesis.build
- https://repo.maven.apache.org/maven2/org/apache/maven/apache-maven/3.9.16/apache-maven-3.9.16-bin.zip
- https://repo1.maven.org/maven2

## 导航

- 项目页：[[10-项目/jenesis.build_7b5dd1ba]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
