---
type: "corpus"
item_id: "c7ff48776160c3bf"
title: "Show HN: Uniflow – a code skeleton so feature #50 looks like feature #1"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=48731598"
project_url: "https://github.com/splendidz/uniflow"
author: "splendidz"
published_at: "2026-06-30T12:14:11Z"
captured_at: "2026-09-21T03:11:00+08:00"
lang: "en"
kind: "post"
topic: SaaS/B2B
shard: "2026-09-21"
pub_day: "2026-06-30"
tags:
  - 语料
  - hn_show
  - author_splendidz
  - story_48731598
  - show_hn
metrics: {"points": 2, "comments": 0, "engagement_velocity": 2}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:113d"
---

# Show HN: Uniflow – a code skeleton so feature #50 looks like feature #1

> [!info] 一句话导读
> Run dozens of concurrent flows on a single thread - a header-only C++17 cooperative-scheduling framework (reactor + worker-pool), zero deps

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=48731598>
> 指标：点赞=2 · 评论=0 · engagement_velocity=2
> 作者：splendidz　|　发布：2026-06-30T12:14:11Z
> 项目链接：<https://github.com/splendidz/uniflow>
> 采集：2026-09-21T03:11:00+08:00　|　id：`c7ff48776160c3bf`

## 正文

# splendidz/uniflow

Run dozens of concurrent flows on a single thread - a header-only C++17 cooperative-scheduling framework (reactor + worker-pool), zero deps

- Stars: 4
- Forks: 0
- Watchers: 4
- Open issues: 0
- License: MIT License
- Homepage: https://splendidz.github.io/uniflow/
- Default branch: develop
- Created: 2026-05-21T13:42:26Z

## Languages

- C#
- C++
- CMake
- Python

## Topics

- async
- automation
- concurrency
- cooperative-scheduling
- cpp
- cpp17
- event-loop
- header-only
- reactor
- state-machine

## Top Contributors

- splendidz (8 contributions)

---

## README

# uniflow

> Language: 한국어 | **English**

ci
C++17
header-only
dependencies
platform
license

```
1 header  |  0 external deps  |  C++17  |  no build system required
```

 Left: dozens of cars driving by the signals in city_traffic  |  Right: two pickers running a line with no zone collision in pick_and_place
 Both demos use zero application-level threads. Every flow runs cooperatively on a single pump thread.

---

## What uniflow is.

uniflow is a **tick-based FSM (finite state machine) asynchronous execution framework**. But not the traditional `switch`-with-`sleep` kind - it strips away the chronic drawbacks of the legacy tick-based FSM with **smart-polling**: instant reaction to events, and yielding the CPU when idle.

Every tick, the pump calls a module's current step once; the step runs to the end without blocking and returns only a step result for what to do next. A step never stops mid-way and runs whole on every call - this execution style is precisely what "run-to-completion" means.

If you have done equipment control or embedded work, the traditional tick-based FSM - ordered logic driven on a single thread - usually looks like this.

```cpp
// the traditional tick-based FSM approach
int step_no = 0;
while (running_)
{
    switch (step_no)
    {
    case 0: Init();   step_no++; break;   // the stage depends on a single integer
    case 1: if (Ready()) step_no++; break;
    case 2: Process(); step_no++; break;
    }
    sleep(10);   // always wait 10ms - the same while working and while idle
}
```

uniflow keeps this exact model, but lets the framework own two things. First, instead of a giant `switch` and an integer `step_no`, the flow is a **chain of named step functions**. Second, instead of a fixed `sleep(10)`, the pump **picks the wait to fit the moment**: no rest while transitions chain, the CPU nearly released while everyone polls for a condition, an immediate `Wake()` when an external event arrives. In short, **not a naive busy-loop.**

The goal of asynchronous processing overlaps with Boost.Asio and C++20 coroutines. The approach, however, differs.

- **Compared to Boost.Asio:** Asio is powerful, but adopting it means taking on a whole set of Asio-family types - `io_context` / `awaitable` / executors - and restructuring your code on top of them. It is specialized for the communication / socket domain. uniflow is **header only with zero dependencies**, and it does not change your existing objects (sockets, file IO, device handles, and so on). It leaves those objects as they are and formalizes only the **logic** that drives them into a step chain. There is no new class methodology to learn, so the adoption cost is low.

- **Compared to C++20 coroutines:** Coroutines are powerful because they are a language feature, but for that same reason they **cannot enforce a style**. How a coroutine is split into units varies from developer to developer, so over time the code fragments again. They also require C++20. uniflow runs on **C++17**, preserving version compatibility with existing projects, and it enforces state at the `task` level. A step jumping incorrectly into a step of another task is **prevented at the framework level (by type and structure)**.

| | Boost.Asio | C++20 coroutines | uniflow |
|---|---|---|---|
| Adoption cost | Learn a set of Asio types | Requires C++20 | 1 header, C++17, no deps |
| Existing objects | Absorbed into Asio types | Free, but no structure | Used as-is, unchanged |
| Development style | Communication-specific | Varies per developer | Enforced via flow / task |
| Observing execution flow | Build it yourself | Build it yourself | Observer built in |

### Core value: structure over async

The primary value of uniflow is not asynchrony itself, but that it **formalizes the way you develop**.

- **A flow / task skeleton that is enforced.** Every time you add a feature, the code does not even come together until you first decide "which exclusive unit (flow) does this belong to" and "which operation (task) is it, split into which steps." In other words, the framework forces one more round of OOP-level design on the developer. When you code freely at the language level, you reason in OOP terms while you have slack, but the moment a deadline closes in you tend to just add one more flag and wedge in one more conditional - whatever makes it work the fastest right now. That rushed code piles up and the structure collapses. In uniflow that shortcut is closed off, so whether you hand the work to an AI or write it yourself, the result is normalized into the same flow / task skeleton. As features and code grow, everything keeps the same shape, so reviews stay consistent; and because code is written in the same structure regardless of a developer's skill, taste, or that day's deadline pressure, the project is structurally prevented from turning into spaghetti over time.
- **A built-in observer.** The framework exposes, as a trace, which step your code is in right now, which operation is in progress, and where it slows down. The execution flow is visible without any separate instrumentation. This is an application-oriented design you can use directly for debugging and operational observability.
- **Use alongside other tools.** uniflow is, in the end, ordinary C++ code, so it can be used together with Asio or coroutines. You set the **development methodology** with uniflow, and bring in the right tool for areas like communication / IO within that frame.

In one line: **it asynchronizes your current logic in a formalized way, without touching your existing objects.**

---

## The three concepts: Flow / Task / Step

uniflow deliberately has only three concepts. Everything else is machinery around them; once these three click, you have the whole model.

**1) A Flow is an object that can run only one Task at a time.** One elevator car (while going up it cannot also go down), one traffic light, one communication link, one motor axis, one order processor. A Flow may hold many Tasks, but at any instant only one of them runs on it - that "one state at a time" object is a Flow. The test is simple: *can two operations overlap on it?* A whole car is a good counterexample, because drive and steering are controlled at the same time; there the car is not one Flow - the drive axis and the steering axis are each a Flow, and several Flows run together. (Running many Flows on a single thread is the heart of uniflow; see the "one thread, no locks" section below.)

**2) A Task is a single unit of work that the Flow performs.** For a drive axis, "drive forward" and "drive backward" are Tasks; for an event processor, "handle event type A" is a Task. One Flow can hold several Tasks but runs only one at a time, and which Task is running is what determines the Flow's current role - this is the core of Flow exclusivity. A Task is "a finite chain of named Steps with a beginning and an end": it starts at `Entry`, chains through sibling Steps, and ends.

**3) A Step is the atomic unit of a Task - a single function.** A Step runs from start to finish, never blocks or waits mid-way, and at the end answers what to do next with exactly one of four results:

- `Next(...)` - advance to the next Step
- `Stay()` - stay on this Step; call me again next round (this is how you wait without blocking - no `while`, no `sleep`)
- `Done()` - this Task finished successfully
- `Fail()` - this Task failed

That is the entire vocabulary. And because a Step's declaration (its name in the list) is separated from its body, reading the function names top to bottom gives you the whole flow at a glance.

---

## Quick Start

With the three concepts above in mind, here is the smallest complete flow. Looking at the declaration and the body separately makes the structure clear at a glance: the declaration (`struct`) is the skeleton of the flow, and the body goes below it (in a real project, in a `.cpp`).

 C++

```cpp
#include "uniflow.hpp"

// One flow = one module. The Uniflow base registers itself with the pump.
class Flow_Example : public uniflow::Uniflow<Flow_Example>
{
public:
    explicit Flow_Example(uniflow::Runtime& rt)
        : uniflow::Uniflow<Flow_Example>(rt, "Example")
    {
        AddTask(task_);                 // wire the task to the flow (one line, once per task)
    }

    // task = a unit of work. It owns its own step member functions. public, so it can be entered from outside.
    struct MyTask : uniflow::Task<Flow_Example>
    {
        StepResult Entry() override { return Step1_Begin(); }   // designate the entry step

    private:                           // the remaining steps are private - reachable only via Entry/Next
        StepResult Step1_Begin();
        StepResult Step2_Work();
        StepResult Step3_Done();
    } task_;

private:
    bool ready_ = true;                // the flow holds the state; steps read it via flow()
};

uniflow::StepResult Flow_Example::MyTask::Step1_Begin()
{
    Describe("initialization complete");  // a one-line description left in the trace/log
    return Next(UF_FN(Step2_Work));    // advance to the next step of the same task
}

uniflow::StepResult Flow_Example::MyTask::Step2_Work()
{
    if (!flow().ready_) return Stay();  // re-poll this step until the condition holds (no blocking)
    return Next(UF_FN(Step3_Done));
}

uniflow::StepResult Flow_Example::MyTask::Step3_Done()
{
    return Done();                     // flow ends normally -> module goes idle
}

int main()
{
    uniflow::Runtime rt;               // spins up one pump thread
    Flow_Example     flow{rt};

    flow.task_.StartFlow();             // callable from any thread
    flow.WaitUntilIdle();
}
```

 Python

```python
import uniflow

# One flow = one module. The Uniflow base registers itself with the pump.
class Flow_Example(uniflow.Uniflow):
    def __init__(self, rt):
        super().__init__(rt, name="Example")
        self.ready = True              # the flow holds the state; steps read it via flow()
        self.task = self.MyTask()
        self.AddTask(self.task)         # wire the task to the flow (one line, once per task)

    # task = a unit of work. It owns its own step methods.
    class MyTask(uniflow.Task):
        def Entry(self):
            return self.Step1_Begin()  # designate the entry step

        def Step1_Begin(self):
            self.Describe("initialization complete")  # a one-line description in the trace/log
            return self.Next(self.Step2_Work)         # advance to the next step of the same task

        def Step2_Work(self):
            if not self.flow().ready:
                return self.Stay()     # re-poll this step until the condition holds (no blocking)
            return self.Next(self.Step3_Done)

        def Step3_Done(self):
            return self.Done()         # flow ends normally -> module goes idle

def main():
    rt = uniflow.Runtime()             # spins up one pump thread
    flow = Flow_Example(rt)

    flow.task.StartFlow()               # callable from any thread
    flow.WaitUntilIdle()
    rt.stop()

if __name__ == "__main__":
    main()
```

 C#

```csharp
using Uniflow;

// One flow = one module. The Module base registers itself with the pump.
sealed class Flow_Example : Module
{
    public bool Ready = true;          // the flow holds the state; steps read it via Flow
    public readonly MyTask TaskT;

    public Flow_Example(Runtime rt) : base(rt, "Example")
    {
        TaskT = new MyTask();
        AddTask(TaskT);                  // wire the task to the flow (one line, once per task)
    }

    // task = a unit of work. It owns its own step methods.
    public sealed class MyTask : Task<Flow_Example>
    {
        protected override StepResult Entry() => Step1_Begin();   // designate the entry step

        StepResult Step1_Begin()
        {
            Describe("initialization complete");  // a one-line description in the trace/log
            return Next(Step2_Work);              // advance to the next step of the same task
        }

        StepResult Step2_Work()
        {
            if (!Flow.Ready) return Stay();        // re-poll until the condition holds (no blocking)
            return Next(Step3_Done);
        }

        StepResult Step3_Done()
        {
            return Done();                         // flow ends normally -> module goes idle
        }
    }
}

static class Program
{
    public static void Main()
    {
        using var rt = new Runtime();              // spins up one pump thread
        var flow = new Flow_Example(rt);

        flow.TaskT.StartFlow();                      // callable from any thread
        flow.WaitUntilIdle();
    }
}
```

---

## The Message Pump

uniflow's unit of execution is the **pump thread**. The core idea is to **not create a thread per concurrent operation**. One `Runtime` owns one pump thread and, on that single thread, cooperatively drives the many flow modules attached to it, visiting each **once per round (round-robin)**. Dozens of flows share one thread. Because of this, shared resources need no lock (lock-free). This does not bind you to a single thread, either - if you need parallelism, create more `Runtime`s to add pump threads. A round proceeds in three stages.

 run each module once -> choose sleep level -> repeat -->

1. **Drain Post** - first, empty the callbacks other threads enqueued via `Post()`. These callbacks run on the pump thread, so they can touch module state without a lock.
2. **Run each module once** - for each active module, call its current step body exactly once. A step returns exactly one of the intents `Stay` / `Next` / `Done` / `Fail` (round-robin, and never blocking).
3. **Choose a sleep level** - based on the busiest module this round, pick how long to wait until the next round.

| This round's result | Next wait | Meaning |
|---|---|---|
| At least one module **advanced** via `Next`/`Done`/`Fail` | `step_interval_sleep_ms` (default 0) | Consecutive transitions go straight to the next round without resting |
| All **polling** via `Stay` | `stay_sleep_ms` (default 20ms) | Normal polling cadence. CPU near 0 |
| All modules **idle** | `idle_sleep_ms` (default 1ms) | Pick up new work quickly |

Two things are key. First, because **every module runs on the same single thread, one at a time**, no locks are needed for shared state between modules (lock-free) - this is the foundation of nearly every advantage that follows. Second, the wait is not a fixed sleep but **decided by the situation**, so when work piles up it proceeds without waiting, and when idle it yields the CPU.

When an external event arrives (a network receive, a sensor interrupt), call `rt.Wake()` from any thread to immediately wake a waiting pump. You do not wait out the pump's sleep.

Thread boundaries are decided **by the designer, not by the unit of work**. Adding more `Runtime`s adds that many pump threads for genuine parallelism; conversely, merging two `Runtime`s onto one pump thread with `Runtime::Link()` makes both sides share the lock-free single-thread invariant again.

---

## Why uniflow

### 1. Smart Polling - a fundamental improvement on the switch/sleep structure

When implementing ordered logic on a single thread, a pattern was commonly used in the past.

```cpp
// the traditional tick-based FSM approach
int step_no = 0;
while (running_)
{
    switch (step_no)
    {
    case 0: Init();   step_no++; break;   // the stage depends on a single integer
    case 1: if (Ready()) step_no++; break;
    case 2: Process(); step_no++; break;
    }
    sleep(10);   // always wait 10ms - the same while working and while idle
}
```

This structure has five problems.

First, the polling period is fixed. Even when stage transitions happen back to back, the sleep gets in the way, hurting responsiveness.

Second, even when an external event arrives (a network receive, a sensor interrupt), the reaction is delayed by up to the sleep duration.

Third, because all the logic piles up inside a single switch block, the function grows bloated as stages increase.

Fourth, **nothing enforces a structure.** You are free to drive the stages with an integer or with a pile of bool flags, so the same logic ends up in completely different shapes from developer to developer. A review has to re-read the flow from scratch every time.

Fifth, **an explicit flow is not guaranteed.** Anywhere, you can assign `step_no = 1` to cut into the middle of a stage. It is hard to track which code jumps where, and the entry point blurs.

uniflow has the message pump choose the wait period to fit the situation (no rest during transitions, yield the CPU when idle), and nails each stage down as a named function, structurally eliminating the five problems above.

When an external event arrives, call `rt.Wake()` from any thread to immediately wake a sleeping pump.

```cpp
// Example. event-receiving thread (a separate thread): when an event arrives,
// immediately wake the runtime (message pump) so a uniflow task can act on it right away.
void OnNetworkReceived(Packet pkt)
{
    module_.SetPendingPacket(pkt);
    runtime_.Wake();         // wake the pump immediately - no sleep wait
}
```

---

### 2. Single Thread, Many Modules - cooperative execution on a single thread

 Left: threads contend for shared state behind locks. Right: one pump thread runs each flow's task steps in turn, so shared state is lock-free.

One `Runtime` owns one pump thread. You can attach as many modules as you like onto this thread, and the pump runs every module once, in order, each round.

```cpp
uniflow::Runtime rt;            // one pump thread

Flow_XAxis    x_axis{rt};       // X-axis task set
Flow_YAxis    y_axis{rt};       // Y-axis task set
Flow_Conveyor conveyor{rt};     // Conveyor task set
Flow_Gripper  gripper{rt};      // Gripper task set

// four modules progress concurrently on one thread - no mutex
x_axis.task_home_.StartFlow();
conveyor.task_run_.StartFlow();
```

Modules on the same `Runtime` share the single-thread invariant, so accessing state between modules needs no mutex. Even in a round where the X axis is `Stay()` polling, the conveyor's stages advance.

Below is a concrete example showing two axes actually moving at the same time. There is only one thread, but while each module waits at its own step with `Stay()`, the other's step runs.

 C++

```cpp
// example: homing the X axis and Y axis at the same time
//
// the traditional way (needs two threads):
//   std::thread t1([]{ x_axis.GoHome(); });   // blocking function
//   std::thread t2([]{ y_axis.GoHome(); });
//   t1.join(); t2.join();
//
// the uniflow way (one thread):
//   x_axis.task_home_.StartFlow();
//   y_axis.task_home_.StartFlow();
//   rt.WaitAll();

// -- Flow_XAxis ---------------------------------
class Flow_XAxis : public uniflow::Uniflow<Flow_XAxis>
{
public:
    Flow_XAxis(uniflow::Runtime& rt) : uniflow::Uniflow<Flow_XAxis>(rt, "XAxis")
    {
        AddTask(task_home_);
    }

    struct Task_Home : uniflow::Task<Flow_XAxis>
    {
        StepResult Entry() override { return Step1_CmdMove(); }
    private:
        StepResult Step1_CmdMove()
        {
            flow().motor_.MoveTo(0);            // issue the move command only, return immediately
            return Next(UF_FN(Step2_Wait));
        }
        StepResult Step2_Wait()
        {
            if (!flow().motor_.InPosition())
                return Stay();                  // still moving - this round ends here
            return Done();                      // complete
        }
    } task_home_;

private:
    Motor motor_;
};

// Flow_YAxis has the same structure (omitted)

// -- run --
uniflow::Runtime rt;
Flow_XAxis x_axis{rt};
Flow_YAxis y_axis{rt};

x_axis.task_home_.StartFlow();   // start homing X
y_axis.task_home_.StartFlow();   // start homing Y (at the same time)

// each pump round:
//   Round 1: X.Step1(cmd move) -> Next  |  Y.Step1(cmd move) -> Next
//   Round 2: X.Step2(moving)   -> Stay  |  Y.Step2(moving)   -> Stay
//   Round N: X.Step2(done)     -> Done  |  Y.Step2(moving)   -> Stay
//   Round M: (X idle)          |  Y.Step2(done) -> Done
//
// while X waits at Stay(), Y runs, and vice versa.
// both axes move at the same time, with no mutex.

x_axis.WaitUntilIdle();
y_axis.WaitUntilIdle();
```

 Python

```python
# example: homing the X axis and Y axis at the same time
#
# the traditional way (needs two threads):
#   t1 = threading.Thread(target=x_axis.go_home)   # blocking function
#   t2 = threading.Thread(target=y_axis.go_home)
#   t1.start(); t2.start(); t1.join(); t2.join()
#
# the uniflow way (one thread):
#   x_axis.task_home.StartFlow()
#   y_axis.task_home.StartFlow()
#   rt.WaitUntilIdle()

# -- Flow_XAxis ---------------------------------
class Flow_XAxis(uniflow.Uniflow):
    def __init__(self, rt):
        super().__init__(rt, name="XAxis")
        self.motor = Motor()
        self.task_home = self.Task_Home()
        self.AddTask(self.task_home)

    class Task_Home(uniflow.Task):
        def Entry(self):
            return self.Step1_CmdMove()

        def Step1_CmdMove(self):
            self.flow().motor.MoveTo(0)          # issue the move command only, return immediately
            return self.Next(self.Step2_Wait)

        def Step2_Wait(self):
            if not self.flow().motor.InPosition():
                return self.Stay()               # still moving - this round ends here
            return self.Done()                   # complete

# Flow_YAxis has the same structure (omitted)

# -- run --
rt = uniflow.Runtime()
x_axis = Flow_XAxis(rt)
y_axis = Flow_YAxis(rt)

x_axis.task_home.StartFlow()   # start homing X
y_axis.task_home.StartFlow()   # start homing Y (at the same time)

# each pump round:
#   Round 1: X.Step1(cmd move) -> Next  |  Y.Step1(cmd move) -> Next
#   Round 2: X.Step2(moving)   -> Stay  |  Y.Step2(moving)   -> Stay
#   Round N: X.Step2(done)     -> Done  |  Y.Step2(moving)   -> Stay
#
# while X waits at Stay(), Y runs, and vice versa.
# both axes move at the same time, with no lock.

x_axis.WaitUntilIdle()
y_axis.WaitUntilIdle()
```

 C#

```csharp
// example: homing the X axis and Y axis at the same time
//
// the traditional way (needs two threads):
//   var t1 = new Thread(() => xAxis.GoHome());   // blocking function
//   var t2 = new Thread(() => yAxis.GoHome());
//   t1.Start(); t2.Start(); t1.Join(); t2.Join();
//
// the uniflow way (one thread):
//   xAxis.TaskHome.StartFlow();
//   yAxis.TaskHome.StartFlow();
//   rt.WaitUntilIdle();

// -- Flow_XAxis ---------------------------------
sealed class Flow_XAxis : Module
{
    public readonly Motor Motor = new Motor();
    public readonly Task_Home TaskHome;

    public Flow_XAxis(Runtime rt) : base(rt, "XAxis")
    {
        TaskHome = new Task_Home();
        AddTask(TaskHome);
    }

    public sealed class Task_Home : Task<Flow_XAxis>
    {
        protected override StepResult Entry() => Step1_CmdMove();

        StepResult Step1_CmdMove()
        {
            Flow.Motor.MoveTo(0);            // issue the move command only, return immediately
            return Next(Step2_Wait);
        }

        StepResult Step2_Wait()
        {
            if (!Flow.Motor.InPosition())
                return Stay();               // still moving - this round ends here
            return Done();                   // complete
        }
    }
}

// Flow_YAxis has the same structure (omitted)

// -- run --
using var rt = new Runtime();
var xAxis = new Flow_XAxis(rt);
var yAxis = new Flow_YAxis(rt);

xAxis.TaskHome.StartFlow();   // start homing X
yAxis.TaskHome.StartFlow();   // start homing Y (at the same time)

// each pump round:
//   Round 1: X.Step1(cmd move) -> Next  |  Y.Step1(cmd move) -> Next
//   Round 2: X.Step2(moving)   -> Stay  |  Y.Step2(moving)   -> Stay
//   Round N: X.Step2(done)     -> Done  |  Y.Step2(moving)   -> Stay
//
// while X waits at Stay(), Y runs, and vice versa.
// both axes move at the same time, with no lock.

xAxis.WaitUntilIdle();
yAxis.WaitUntilIdle();
```

Genuinely blocking work (I/O, heavy computation) is delegated to the built-in thread pool via `SubmitAsync`, which wakes the pump on completion. The pump thread itself is never blocked.

Creating multiple `Runtime`s yields multiple pump threads. With `Runtime::Link()` you can also merge two runtimes onto a single pump thread.

---

### 3. Flat Structure - flat code structure and team consistency

Take a task any robot orchestration layer has to write. On ROS2, the orchestrator sends a move command to the motion module, waits for the arrival reply, and only then turns the camera on and inspects a frame. A command you send and the reply you expect back are a logical **pair** - but in a callback- or thread-split design that pairing is nowhere in the code.

```cpp
// ROS2 callback style - the protocol is smeared across a constructor, a sender,
// two subscription callbacks, a spin thread, and a bag of flags behind a lock.
class PickNode : public rclcpp::Node
{
public:
    PickNode() : Node("pick")
    {
        goal_pub_   = create_publisher<MotionGoal>("/motion/goal", 10);
        cam_client_ = create_client<EnableCamera>("/camera/enable");
        // the two replies we care about arrive on subscriptions, wired up here -
        // far from where the command will actually be sent
        result_sub_ = create_subscription<MotionResult>(
            "/motion/result", 10, this { OnMotionResult(m); });
        frame_sub_  = create_subscription<Image>(
            "/camera/frame", 10, this { OnFrame(m); });
        // callbacks fire on the executor thread; StartPick is called from another -
        // so every shared flag below now needs a lock
        spin_thread_ = std::thread([this] { rclcpp::spin(shared_from_this()); });
    }

    void StartPick(const Pose& target)
    {
        std::lock_guard<std::mutex> lk(mu_);
        goal_pub_->publish(MakeGoal(target));        // fire the command...
        waiting_arrival_ = true;                     // ...and remember, by hand, what we now expect
        // nothing here waits - control returns to the caller immediately
    }

private:
    // fires at some unknown later time, on the executor thread, for some reply
    void OnMotionResult(MotionResult::SharedPtr msg)
    {
        std::lock_guard<std::mutex> lk(mu_);
        if (!waiting_arrival_) return;               // is this reply even for us? guess from a flag
        waiting_arrival_ = false;
        if (!msg->ok) { fault_ = true; return; }     // failure handling, stranded far from the send site
        cam_client_->async_send_request(std::make_shared<EnableCamera::Request>());
        waiting_frame_ = true;                        // a second expectation - a second flag
    }

    void OnFrame(Image::SharedPtr msg)
    {
        std::lock_guard<std::mutex> lk(mu_);
        if (!waiting_frame_) return;
        waiting_frame_ = false;
        Inspect(msg);
        // a late frame from a goal we already gave up on lands here too - the flags
        // cannot tell which goal it belonged to, so a stale message takes the live path
    }

    rclcpp::Publisher<MotionGoal>::SharedPtr      goal_pub_;
    rclcpp::Client<EnableCamera>::SharedPtr       cam_client_;
    rclcpp::Subscription<MotionResult>::SharedPtr result_sub_;
    rclcpp::Subscription<Image>::SharedPtr        frame_sub_;
    std::thread spin_thread_;
    std::mutex  mu_;
    bool waiting_arrival_ = false;   // the whole protocol, reduced to a bag of flags
    bool waiting_frame_   = false;
    bool fault_           = false;
    // and the "no reply at all within 10s" timeout? it lives nowhere yet - it would
    // need its own timer, its own callback, and a reset on every path above
};
```

Read `StartPick` alone and you cannot tell what happens after the command goes out. Read `OnMotionResult` alone and you cannot tell what command it answers, or when it fires. The sequence "send goal -> await arrival -> enable camera -> await frame -> inspect" lives only in the developer's head; the code smears it across a constructor, a sender, and two callbacks stitched together by `waiting_arrival_`/`waiting_frame_`. Because a callback runs whenever a message happens to land - on a different thread, hence the lock - the timing is invisible, a stale reply to an abandoned goal follows the exact same path as a fresh one, and the one thing the diagram would show most clearly, the 10-second "the reply never came" timeout, has no home at all.

In uniflow the command and the reply it expects sit right next to each other, and the flow waits for that reply at the very spot it sent the command.

```cpp
StepResult Step1_SendGoal()
{
    flow().motion_.SendGoal(target_);                 // send the move command...
    return Next(UF_FN(Step2_WaitArrived));            // ...expecting an arrival reply next
}

StepResult Step2_WaitArrived()
{
    if (!flow().motion_.HasReply())
        return StayTimeout(10s, UF_FN(Step_Abort));   // wait right here; no reply in 10s -> abort
    if (!flow().motion_.Reply().ok) return Fail();    // arrived, but the module refused
    return Next(UF_FN(Step3_EnableCamera));           // arrived ok -> now, and only now, the camera
}

StepResult Step3_EnableCamera()
{
    flow().camera_.Enable();
    return Next(UF_FN(Step4_WaitFrame));
}

StepResult Step4_WaitFrame()
{
    if (!flow().camera_.HasFrame()) return Stay();    // wait right here for the frame
    flow().Inspect(flow().camera_.TakeFrame());
    return Done();
}

StepResult Step_Abort()
{
    flow().motion_.Cancel();
    return Fail();
}
```

The command and the reply it waits for are adjacent: `Step1` sends, `Step2` right below it is the wait for that command's answer. The expectation is written down - "I sent a goal, so I wait for a goal reply, and nothing else advances until it arrives (or 10s pass)." There are no `waiting_*` flags, because "which reply am I waiting for" is simply "which step am I in." A stale reply to an already-abandoned goal cannot slip through, because the flow is not listening for it - it is parked on `Step2` or has already moved past it. `Step_Abort` carries no number because it is an off-path exit, not another stage in the sequence.

And here is the decisive part: the steps above **are** a state chart. Read the code top to bottom and you trace the exact same path as reading the diagram below - every step is one node, and every `return` (`Next`/`Stay`/`StayTimeout`/`Done`/`Fail`) is one labeled edge. There is no translation step between "the diagram the engineer drew on the whiteboard" and "the code that ships."

State chart maps 1:1 to uniflow steps

This is what the callback version cannot offer. There, a state like "goal sent, waiting for arrival" exists only as `waiting_arrival_ == true` spread across two handlers - you cannot point at it in a diagram, and you cannot point at it in the code either. In uniflow that state is literally `Step2_WaitArrived`, one named function you can point at, set a breakpoint on, and match to one box in the chart.

This structure also helps in team work. Because every developer expresses request/reply logic in the same pattern, the sequence is grasped immediately in code review. Because the framework enforces the pattern, consistent code results regardless of experience level.

---

### 4. Built-in Tracing - built-in tracing and observability

Because every execution reduces to the single shape "a step function was called once," a single measurement point inside the pump observes the entire flow. Using the default `ConsoleObserver`, the following information is recorded automatically, with no separate logging code.

```
[JobWorker    ] FLOW START  caller=main.cpp:42 main()
[JobWorker    ] Entry -> Step2_Validate                         #00 elapsed=0.01ms  tick x8 avg=0.01ms
[JobWorker    ]                 ASYNC SUBMIT  CallApi
[JobWorker    ]                 ASYNC DONE    CallApi  wait=124.38ms
[JobWorker    ] Step2_Validate -> Step3_WaitSave  inserted=3000  #01 elapsed=124.42ms tick x1 avg=0.03ms
[JobWorker    ] Step3_WaitSave -> Done                           #02 elapsed=18.71ms  tick x1
[JobWorker    ] FLOW END  DONE  steps=#02  wall=143.21ms  step=0.07ms  async=143.09ms  tick x10 avg=0.01ms
```

Each line contains the transition from the previous stage to the next, the time spent in that stage, body run statistics, async wait time, and the description set with `Describe()`.

Slow-step alarms, slow-async-job alarms, and round-level profiling are also configurable.

```cpp
uniflow::Runtime::Opts opts;
opts.config.slow_step_threshold_ms  = std::chrono::milliseconds(10);   // warn when a step body exceeds 10ms
opts.config.slow_async_threshold_ms = std::chrono::milliseconds(500);  // warn when an async job exceeds 500ms
uniflow::Runtime rt{std::move(opts)};
```

To connect to your own metrics system or alerting channel, derive from `IUniflowObserver` and override only the hooks you need. Because the measurement point is in one place rather than scattered throughout the logic code, instrumentation code and business logic stay separated.

---

### 5. Task - unit-based type safety + explicit transitions (Type-safe Units)

As steps grow numerous, it becomes hard to tell which step belongs to which logical operation. uniflow groups related steps into a struct deriving from `uniflow::Task `. A task directly owns its own step member functions, so each step belongs, by definition, to its task.

 C++

```cpp
class Flow_PickPlace : public uniflow::Uniflow<Flow_PickPlace>
{
public:
    explicit Flow_PickPlace(uniflow::Runtime& rt)
        : uniflow::Uniflow<Flow_PickPlace>(rt, "PickPlace")
    {
        AddTask(task_pick_);
        AddTask(task_place_);
    }

    // public - the orchestrator enters the desired unit directly via task.StartFlow()
    struct Task_Pick : uniflow::Task<Flow_PickPlace>
    {
        int part_id = 0;                               // state shared by the steps within the task
        StepResult Entry() override { return Step1_MoveToSource(); }

    private:
        StepResult Step1_MoveToSource()
        {
            part_id = flow().source_.NextPart();
            return Next(UF_FN(Step2_WaitAtSource));
        }

        StepResult Step2_WaitAtSource()
        {
            if (!flow().arm_.IsReady()) return Stay();
            flow().task_place_.slot = flow().dest_.FreeSlot();
            return StartTask(flow().task_place_);       // switch to Task_Place
        }
    } task_pick_;

    struct Task_Place : uniflow::Task<Flow_PickPlace>
    {
        int slot = 0;
        StepResult Entry() override { return Step1_MoveToDest(); }

    private:
        StepResult Step1_MoveToDest()
        {
            flow().arm_.MoveTo(flow().dest_pos_[slot]);
            return Next(UF_FN(Step2_Release));
        }

        StepResult Step2_Release() { flow().arm_.Release(); return Done(); }
    } task_place_;
};
```

 Python

```python
class Flow_PickPlace(uniflow.Uniflow):
    def __init__(self, rt):
        super().__init__(rt, name="PickPlace")
        self.task_pick = self.Task_Pick()
        self.AddTask(self.task_pick)
        self.task_place = self.Task_Place()
        self.AddTask(self.task_place)

    # public - the orchestrator enters the desired unit directly via task.StartFlow()
    class Task_Pick(uniflow.Task):
        def __init__(self):
            super().__init__()
            self.part_id = 0                               # state shared by the steps in the task

        def Entry(self):
            return self.Step1_MoveToSource()

        def Step1_MoveToSource(self):
            self.part_id = self.flow().source.NextPart()
            return self.Next(self.Step2_WaitAtSource)

        def Step2_WaitAtSource(self):
            if not self.flow().arm.IsReady():
                return self.Stay()
            self.flow().task_place.slot = self.flow().dest.FreeSlot()
            return self.StartTask(self.flow().task_place)   # switch to Task_Place

    class Task_Place(uniflow.Task):
        def __init__(self):
            super().__init__()
            self.slot = 0

        def Entry(self):
            return self.Step1_MoveToDest()

        def Step1_MoveToDest(self):
            self.flow().arm.MoveTo(self.flow().dest_pos[self.slot])
            return self.Next(self.Step2_Release)

        def Step2_Release(self):
            self.flow().arm.Release()
            return self.Done()
```

 C#

```csharp
sealed class Flow_PickPlace : Module
{
    public readonly Task_Pick TaskPick;
    public readonly Task_Place TaskPlace;

    public Flow_PickPlace(Runtime rt) : base(rt, "PickPlace")
    {
        TaskPick = new Task_Pick();
        AddTask(TaskPick);
        TaskPlace = new Task_Place();
        AddTask(TaskPlace);
    }

    // public - the orchestrator enters the desired unit directly via TaskT.StartFlow()
    public sealed class Task_Pick : Task<Flow_PickPlace>
    {
        public int PartId;                                 // state shared by the steps in the task
        protected override StepResult Entry() => Step1_MoveToSource();

        StepResult Step1_MoveToSource()
        {
            PartId = Flow.Source.NextPart();
            return Next(Step2_WaitAtSource);
        }

        StepResult Step2_WaitAtSource()
        {
            if (!Flow.Arm.IsReady()) return Stay();
            Flow.TaskPlace.Slot = Flow.Dest.FreeSlot();
            // In C#, StartTask returns StartResult (not StepResult), so a step cannot
            // "return StartTask(...)". Finish this task and let the orchestrator launch
            // Task_Place via StartFlow() the way the pick_and_place example does.
            return Done();
        }
    }

    public sealed class Task_Place : Task<Flow_PickPlace>
    {
        public int Slot;
        protected override StepResult Entry() => Step1_MoveToDest();

        StepResult Step1_MoveToDest()
        {
            Flow.Arm.MoveTo(Flow.DestPos[Slot]);
            return Next(Step2_Release);
        }

        StepResult Step2_Release()
        {
            Flow.Arm.Release();
            return Done();
        }
    }
}

// orchestrate Pick -> Place: Pick finishes, then the orchestrator launches Place.
//   flow.TaskPick.StartFlow();  flow.WaitUntilIdle();
//   flow.TaskPlace.StartFlow(); flow.WaitUntilIdle();
```

A step is a member of its own task and so belongs to it, and `Next` points only to a sibling step. To move to another unit, cross the task boundary explicitly with `StartTask`. Because the unit boundary shows up directly in the code structure, it never gets blurry which step belongs to which unit.

**The key point is that transitions are pinned explicitly in the code.** Each step names its next step directly with `Next(UF_FN(...))`, and that target can only be a sibling step of the same task. So **just by scanning the function declaration list**, it becomes clear in what order the logic must be called - where it starts (`Entry`) and where it flows. There is no way to cut into the middle of a stage from outside (steps are `private`; entry is only via `Entry`), so there are no hidden entry points and no untraceable jumps. The flow is fixed by type and declaration, which greatly improves reada

## 关联链接

- https://splendidz.github.io/uniflow/

## 导航

- 项目页：[[10-项目/github.com_0dc72bc5]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`SaaS/B2B`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
