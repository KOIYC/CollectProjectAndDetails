---
type: "corpus"
item_id: "64e8dab152963cc0"
title: "Show HN: Tilery-VM – run Nvidia cuTile GPU kernels on a CPU, no GPU required"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49111222"
project_url: "https://github.com/drbh/tilery-vm"
author: "justdrbh"
published_at: "2026-07-30T15:14:36Z"
captured_at: "2026-09-21T03:11:16+08:00"
lang: "en"
kind: "post"
topic: "开发者工具"
shard: "2026-09-21"
pub_day: "2026-07-30"
tags:
  - 语料
  - hn_show
  - author_justdrbh
  - story_49111222
  - show_hn
metrics: {"points": 4, "comments": 0, "engagement_velocity": 4}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:83d"
---

# Show HN: Tilery-VM – run Nvidia cuTile GPU kernels on a CPU, no GPU required

> [!info] 一句话导读
> CPU virtual machine for CUDA Tile IR bytecode - run cuTile kernels without a GPU

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49111222>
> 指标：点赞=4 · 评论=0 · engagement_velocity=4
> 作者：justdrbh　|　发布：2026-07-30T15:14:36Z
> 项目链接：<https://github.com/drbh/tilery-vm>
> 采集：2026-09-21T03:11:16+08:00　|　id：`64e8dab152963cc0`

## 正文

# drbh/tilery-vm

CPU virtual machine for CUDA Tile IR bytecode - run cuTile kernels without a GPU

- Stars: 0
- Forks: 0
- Watchers: 0
- Open issues: 0
- License: Apache License 2.0
- Default branch: main
- Created: 2026-03-24T18:09:57Z

## Languages

- MLIR
- Makefile
- Python
- Rust
- Shell

## Topics

- cuda
- cutile
- gpu-programming
- interpreter
- mlir
- rust
- tileir
- virtual-machine

## Top Contributors

- drbh (20 contributions)

---

## README

# tilery-vm

`tilery-vm` is a virtual machine for CUDA Tile IR bytecode.

It executes TileIR bytecode on a CPU, so cuTile kernels can be developed and
tested without a GPU. TileIR is NVIDIA's open, language-agnostic IR for CUDA
kernels (the PTX analogue for the tile programming model); cuTile is the
user-facing language that emits it, from both the Python and Rust clients.

## Quickstart

no GPU, no CUDA, no setup step:

```bash
uv run examples/minimal.py   # [0.0320586  0.08714432 0.23688284 0.6439143 ]
cargo test --workspace       # 136 tests
```

## Usage

One way you can use `tilery-vm` is by using tilery_vm as a cpu backend for `cuda-tile`.

This allows you to write native cutile in a environment that does not have a gpu, and run it on the cpu.

python client example
```python
# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "cuda-tile[tileiras]==1.4.0; sys_platform != 'darwin'",
#     "cuda-tile==1.4.0; sys_platform == 'darwin'",
#     "numpy",
#     "tilery-vm",
# ]
#
# [tool.uv.sources]
# tilery-vm = { path = "../bindings" }
# cuda-tile = { path = "../parity/osx-cutile/cutile-shim", marker = "sys_platform == 'darwin'" }
# ///
import tilery_vm.cpu  # noqa: F401

import cuda.tile as ct
import numpy as np

@ct.kernel
def softmax(a, result):
    x = ct.load(a, index=(0,), shape=(4,))
    e = ct.exp(x - ct.max(x, axis=0))
    ct.store(result, index=(0,), tile=e / ct.sum(e, axis=0))

a = np.array([1, 2, 3, 4], dtype=np.float32)
result = np.zeros(4, dtype=np.float32)
ct.launch(None, (1, 1, 1), softmax, (a, result))

print(result)  # [0.0320586  0.08714432 0.23688284 0.6439143 ]
```

or from rust

rust client example
```rust
use cutile::compile_api::KernelCompiler;
use tilery_vm::{Arg, launch};

#[cutile::module]
mod my_kernels {
    use cutile::core::*;

    /// out[i] = scalar + 1, for a length-`S` f32 tensor.
    #[cutile::entry()]
    fn add_scalar<const S: [i32; 1]>(output: &mut Tensor<f32, S>, scalar: f32) {
        let scalar_tile: Tile<f32, S> = broadcast_scalar(scalar, output.shape());
        let ones: Tile<f32, S> = broadcast_scalar(1.0f32, output.shape());
        output.store(scalar_tile + ones);
    }
}

fn main() {
    // compile the DSL kernel to bytecode
    let artifacts =
        KernelCompiler::new(my_kernels::__module_ast_self, "my_kernels", "add_scalar")
            .generics(vec!["8".into()]) // const S = [8]
            .strides(&[("output", &[1])])
            .target("sm_89")
            .compile()
            .expect("DSL compile failed");
    let bytecode = artifacts.bytecode().expect("bytecode serialization failed");

    // run it on the CPU - pass a tensor + a scalar, just like a launch
    let mut output = vec![0.0_f32; 8];
    launch(&bytecode, [1, 1, 1], &mut [Arg::tensor(&mut output), Arg::f32(5.0)])
        .expect("run on CPU");

    println!("\noutput = {output:?}"); // scalar + 1 = [6, 6, 6, 6, 6, 6, 6, 6]
}
```

## How it works

this repo contains a tileir mlir parser that converts the mlir into a executable module. the repo also contains a interpreter that can execute the module on the cpu. the interpreter is designed to be simple and easy to understand, and can be used as a reference for implementing other backends.

we also support processing tileir bytecode directly, which we first deserialize into a module, and then follow the existing interpreter path to execute the module on the cpu.

tileir bytecode is the canonical representation of a compiled tile kernel, and is what the cuTile clients (Python and Rust) emit. on a GPU that bytecode is handed to NVIDIA's `tileiras` assembler, which lowers it to a cubin for a specific target. tilery-vm consumes the same bytecode and interprets it directly, which is what lets cuTile kernels run on any cpu.

## Correctness

correctness is the whole point of this VM, so here is precisely what is verified
today and what is not. ~89 op forms are implemented end-to-end (parse + execute).

#### op-level goldens captured from real hardware

`crates/tilery-vm/optests/` holds **90 op cases** (`optests.mlir` + `cases.json`,
kept 1:1 by a test). **69 of them carry expected values captured from real cuTile
on an NVIDIA RTX 4090** (sm_89, cuda-tile 1.4.0) by `parity/cutile_capture.py` and
stored in `optests/cutile_goldens.json` - all 69 match the VM. this is a stored
capture from one device configuration, not something re-run on every build.

the remaining 21 cases have no GPU golden. they are the memory/view/pointer/token
surface (`make_tensor_view`, `load_ptr_tko`, `reshape`, `permute`, `offset`, ...)
and are checked against hand-written expectations only.

#### live GPU parity (requires an NVIDIA GPU)

`parity/bytecode_parity.py` runs **7 kernels** (`vadd`, `loopadd`, `row_sum`,
`row_cumsum`, `gemm`, `softmax`, `atom`) through the *same* client-emitted
bytecode on both a real GPU and the VM, comparing f32 outputs at `atol = rtol =
1e-4`. needs `cupy` and a real device.

```bash
uv run parity/bytecode_parity.py
```

#### unit tests (cpu only)

```bash
cargo test --workspace
```

136 tests: 97 parser tests (textual IR -> module), the 90-case optest table, plus
interpreter, lexer and memory tests. no test in the rust suite touches a GPU.

`--workspace` matters: this workspace sets `default-members = ["crates/tilery-vm"]`,
so a bare `cargo test` runs only 101 of them and skips the `tilery-parser` and
`tilery-interpreter` unit tests.

#### parser coverage vs the upstream dialect

```bash
parity/fetch_reference_corpus.sh
uv run parity/op_parity.py
```

this is *static* analysis - it diffs our parser's op dispatch against upstream's
`Ops.td` and reports which mnemonics appear in our local `.mlir` corpus. it does
not execute anything; executed evidence is the two sections above.

#### known limitations

- **`f16` / `bf16` / `tf32` are accepted but represented as `f32`.** that is sound
 for MMA (16-bit in, f32 accumulate) but *not* for elementwise chains, where
 hardware rounds at every step and the VM does not. raw sub-f32 buffer I/O is
 also wrong-width. there is no GPU parity evidence below f32 - everything above
 is f32/f64/int.
- `i16`, unsigned-as-distinct-types, and sub-byte floats (`f8E*`, `f4E*`) are not
 implemented; pointer buffers are rejected.
- an unknown mnemonic surfaces as a generic parse error rather than a
 "unsupported op" diagnostic.
- the interpreter is scalar, so a large forward pass takes seconds - this is a
 fidelity tool, not a fast runtime.
- no CI yet; the parity scripts print results but do not gate on failure.

## License

Apache-2.0 - see LICENSE.

this project is not affiliated with or endorsed by NVIDIA. it interoperates with
`cuda-tile` (Apache-2.0) as a client; no NVIDIA source is vendored into this repo.
the macOS shim under `parity/osx-cutile/` builds against a wheel downloaded from
PyPI at build time - see `parity/osx-cutile/README.md`.

# chatcode-lab/stock-tui

## 导航

- 项目页：[[10-项目/github.com_402570a5]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`开发者工具`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
