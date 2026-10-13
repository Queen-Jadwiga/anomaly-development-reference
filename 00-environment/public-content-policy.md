# Public research content and privacy

> ADR document set: **v0.1.84**. Research revisions and source/build versions below describe their original scope.

ADR publishes reusable technical findings, source/build versions, source-file hashes, contract evidence and aggregate test outcomes. A private intake is not permission to publish every fact in the attached file.

Keep personal names, usernames, profile labels, installation/home paths, exact session timestamps, hardware/network/account details, raw logs/modlists/saves and private upload/executable fingerprints outside public documentation. Public immutable commit references and public code-file pins may remain when needed for reproducibility; uploaded-package fingerprints, collected private file fingerprints and archive paths are withheld. Use opaque evidence IDs for private observations and state that independent readers cannot reproduce them from public artifacts alone.

The v0.1.84 audit removes uploaded-package fingerprints and personal log identifiers and withdraws the installation-derived supplement/evidence tables from the current public tree. Its working evidence is retained privately. Reusable upstream-source research, public source pins and useful tools remain. Raw logs, modlists, saves and private source collections are not public deliverables.

The automated [public-content check](../tools/check_public_content.py) catches common personal-log and local-machine path leaks. It is a bounded guard, not a guarantee: manually review new intake metadata before publication. Run it with the [repository checker](../tools/check_repository.py).

## Git history boundary

Current-file cleanup does not erase old commits, immutable links, cloned copies, cached content or author/committer metadata. Previously published material remains recoverable in earlier revisions. A separate coordinated rewrite would need to enumerate affected refs/commits, retain the useful history, update public provenance links and coordinate clones; cached copies may require provider support. No history rewrite is claimed here.

New commit author/committer identity follows the connected publishing account. Removing repository text does not change that account's email/identity or rewrite earlier attribution. Review the publishing account's public identity separately if that is part of the desired privacy boundary.

