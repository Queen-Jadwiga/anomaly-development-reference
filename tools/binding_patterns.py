"""Registration forms recognized after preprocessing the scoped native sources.
Property expressions are preserved; this helper does not infer converter/signature policy.
"""
import re
BINDING_PATTERN = re.compile(r'(?<!\w)(\.def(?:_readonly|_readwrite)?|\.property|(?<!\.)\bdef)\s*\(')

def binding_kind(form, expression):
    return {'constructor':'constructor', '.def_readonly':'readonly_field',
            '.def_readwrite':'writable_field', '.property':'property',
            'def':'global_function'}.get(form, 'virtual_method' if '_static' in expression else 'method')

def valid_binding_origin(line):
    return 'def' in line or 'property' in line or 'luabind_class_' in line
