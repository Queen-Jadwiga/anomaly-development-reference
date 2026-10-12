# Debugging workflow

> ADR document set: **v0.1.67**. Research revisions and source/build versions below describe their original scope.

1. Keep original log and timestamp privately.
2. Extract startup banner and environment facts.
3. Preserve full error + traceback + affected mod revision.
4. Identify the smallest reproduction and record expected/observed result.
5. Label hypotheses separately from confirmed causes.
6. Test minimal fix, then regression test the full mod.
7. Add findings to relevant API notes with evidence IDs.

Never publish personal machine paths or unredacted logs by default.
