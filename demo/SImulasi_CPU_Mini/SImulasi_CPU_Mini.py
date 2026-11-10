program = [("LOAD", 5), ("ADD", 3), ("STORE", None)]
akumulator = 0

for pc, instruksi in enumerate(program):
    print(f"[FETCH]   ambil instruksi ke-{pc}: {instruksi}")
    op, nilai = instruksi
    print(f"[DECODE]  operasi  = {op}")
    if op == "LOAD":
        akumulator += nilai
    elif op == "ADD":
        akumulator += nilai
    print(f"[EXECUTE] akumulator = {akumulator}")
    print(f"[WRITEBACK] hasil disimpan ke register\n")
