

# 3. Napisati funkciju koja kao parametar prima broj i vraća True ako su prva i
# zadnja znamenka broja jednake. U suprotnom vraća False.

def jednake(broj):
    # 12451
    zadnja = broj % 10
    while broj >= 10:
        broj //=10
    return zadnja == broj

print(jednake(12451))
print(jednake(32451))