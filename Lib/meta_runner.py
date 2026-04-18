#!/usr/bin/env python by dwi bakti n dev
import sys
import re
import traceback
import os
import builtins
import math
import random
import datetime
import json
import ctypes
import platform
from pathlib import Path
from typing import Any, Dict, List, Tuple, Optional

# ==================== ICON DAN BRANDING ====================

class MetaBranding:
    """Class untuk menangani branding dan icon Meta Language"""
    
    @staticmethod
    def get_icon_path() -> Optional[Path]:
        """Mendapatkan path ke file icon"""
        # Cek beberapa lokasi yang mungkin
        possible_paths = [
            Path(__file__).parent / "lib" / "meta_icon" / "icon.ico",
            Path.cwd() / "lib" / "meta_icon" / "icon.ico",
            Path.home() / ".meta" / "icon.ico",
            Path(sys.prefix) / "share" / "meta" / "icon.ico" if hasattr(sys, 'prefix') else None,
        ]
        
        for path in possible_paths:
            if path and path.exists():
                return path
        return None
    
    @staticmethod
    def set_console_title(title: str = "Meta Language"):
        """Mengatur judul console window"""
        try:
            if platform.system() == "Windows":
                ctypes.windll.kernel32.SetConsoleTitleW(title)
            else:
                # Untuk Unix-like systems, gunakan ANSI escape codes
                sys.stdout.write(f"\033]0;{title}\007")
                sys.stdout.flush()
        except:
            pass
    
    @staticmethod
    def set_console_icon():
        """Mengatur icon console window (Windows only)"""
        if platform.system() != "Windows":
            return
        
        icon_path = MetaBranding.get_icon_path()
        if not icon_path:
            return
        
        try:
            # Load icon menggunakan Windows API
            hwnd = ctypes.windll.kernel32.GetConsoleWindow()
            if hwnd:
                # WM_SETICON = 0x80
                # ICON_SMALL = 0, ICON_BIG = 1
                icon_handle = ctypes.windll.user32.LoadImageW(
                    0, str(icon_path), 1, 0, 0, 0x00000010  # IMAGE_ICON, LR_LOADFROMFILE
                )
                if icon_handle:
                    ctypes.windll.user32.SendMessageW(hwnd, 0x0080, 0, icon_handle)  # ICON_SMALL
                    ctypes.windll.user32.SendMessageW(hwnd, 0x0080, 1, icon_handle)  # ICON_BIG
        except:
            pass
    
    @staticmethod
    def print_banner():
        """Menampilkan banner Meta Language"""
        banner = f"""
    ╔══════════════════════════════════════════════════════════════════════════════════╗
    ║                                                                                  ║
    ║                    ███╗   ███╗███████╗████████╗ █████╗                           ║
    ║                    ████╗ ████║██╔════╝╚══██╔══╝██╔══██╗                          ║
    ║                    ██╔████╔██║█████╗     ██║   ███████║                          ║
    ║                    ██║╚██╔╝██║██╔══╝     ██║   ██╔══██║                          ║
    ║                    ██║ ╚═╝ ██║███████╗   ██║   ██║  ██║                          ║
    ║                    ╚═╝     ╚═╝╚══════╝   ╚═╝   ╚═╝  ╚═╝                          ║
    ║                                                                                  ║
    ║                          LANGUAGE INTERPRETER v1.0                               ║
    ║                     Bahasa Pemrograman dengan Sintaks Indonesia                  ║
    ║                                                                                  ║
    ╚══════════════════════════════════════════════════════════════════════════════════╝
    
    📍 Dibuat dengan ❤️  oleh Dwi Bakti N Dev
    🌐 Website: https://portofolio-dwi-bakti-n-dev-liard.vercel.app/
    📧 Email: Dwibakti76@gmail.com
    
    ──────────────────────────────────────────────────────────────────────────────────
    """
        print(banner)
    
    @staticmethod
    def print_logo_small():
        """Menampilkan logo kecil"""
        logo = """
    ╭─────────────────────────────────────────────────────────────────────────────────╮
    │                              META LANGUAGE v1.0                                 │
    │                         Sintaks Indonesia, Kekuatan Meta                        │
    ╰─────────────────────────────────────────────────────────────────────────────────╯
    """
        print(logo)


class MetaInterpreter:
    """
    MetaInterpreter - Interpreter untuk bahasa pemrograman Meta Language
    Bahasa pemrograman berbasis Python dengan sintaks Bahasa Indonesia
    """
    
    def __init__(self):
        """Inisialisasi interpreter dengan aturan konversi dan konteks global"""
        
        # Aturan konversi regex (pola, pengganti)
        self.konversi_rules: List[Tuple[str, str]] = [
            # ==================== LIST COMPREHENSION (HARUS PALING ATAS) ====================
            (r'\[([^\[]*?)\s+untuk\s+(\w+)\s+dalam\s+([^\]]+?)(?:\s+jika\s+([^\]]+?))?\]',
             lambda m: self._convert_list_comprehension(m)),
            
            (r'\{([^\[]*?)\s+untuk\s+(\w+)\s+dalam\s+([^\}]+?)(?:\s+jika\s+([^\}]+?))?\}',
             lambda m: self._convert_dict_comprehension(m)),
            
            # ==================== INPUT FUNCTION ====================
            (r'\bmasukan\s*\(', 'input('),
            (r'\bbaca\s*\(', 'input('),
            
            # ==================== OUTPUT FUNCTIONS ====================
            (r'\bmeta\s*\(', 'print('),
            (r'\bcetak\s*\(', 'print('),
            (r'\btulis\s*\(', 'print('),
            
            # ==================== TYPE CONVERSION ====================
            (r'\bteks\s*\(', 'str('),
            (r'\bbilangan\s*\(', 'int('),
            (r'\bangka\s*\(', 'int('),
            (r'\bdesimal\s*\(', 'float('),
            (r'\blist\s*\(', 'list('),
            (r'\bdictionary\s*\(', 'dict('),
            (r'\btuple\s*\(', 'tuple('),
            (r'\bset\s*\(', 'set('),
            (r'\bbenar_salah\s*\(', 'bool('),
            
            # ==================== MATH FUNCTIONS ====================
            (r'\bakar\s*\(', 'math.sqrt('),
            (r'\babsolut\s*\(', 'abs('),
            (r'\bbulatkan\s*\(', 'round('),
            (r'\bpangkat\s*\(', 'pow('),
            (r'\bmaksimal\s*\(', 'max('),
            (r'\bminimal\s*\(', 'min('),
            (r'\bjumlah\s*\(', 'sum('),
            
            # ==================== BUILT-IN FUNCTIONS ====================
            (r'\brentang\s*\(', 'range('),
            (r'\bpanjang\s*\(', 'len('),
            (r'\btipe\s*\(', 'type('),
            (r'\benumerasi\s*\(', 'enumerate('),
            (r'\bzip\s*\(', 'zip('),
            (r'\bpetakan\s*\(', 'map('),
            (r'\bsaring\s*\(', 'filter('),
            (r'\burutkan\s*\(', 'sorted('),
            
            # ==================== IMPORT STATEMENTS ====================
            (r'^(\s*)dari\s+([\w\.]+)\s+import\s+(.+)$', r'\1from \2 import \3'),
            (r'^(\s*)import\s+(.+)$', r'\1import \2'),
            
            # ==================== FUNCTION DEFINITION ====================
            (r'^(\s*)modul\s+(\w+)\s*\((.*)\)\s*:?$', r'\1def \2(\3):'),
            (r'^(\s*)modul\s+(\w+)\s*:?$', r'\1def \2():'),
            (r'^(\s*)fungsi\s+(\w+)\s*\((.*)\)\s*:?$', r'\1def \2(\3):'),
            
            # ==================== RETURN STATEMENT ====================
            (r'^(\s*)kembalikan\s+(.+)$', r'\1return \2'),
            (r'^(\s*)kembalikan\s*$', r'\1return'),
            (r'^(\s*)fungsi\s+(.+)$', r'\1return \2'),
            
            # ==================== CONDITIONAL STATEMENTS ====================
            (r'^(\s*)jika\s+(.+?)\s+maka\s*:?$', r'\1if \2:'),
            (r'^(\s*)atau\s+jika\s+(.+?)\s+maka\s*:?$', r'\1elif \2:'),
            (r'^(\s*)selain\s+itu\s*:?$', r'\1else:'),
            
            # ==================== LOOP STATEMENTS ====================
            (r'^(\s*)untuk\s+(\w+)\s+dalam\s+(.+?)\s*:?$', r'\1for \2 in \3:'),
            (r'^(\s*)selama\s+(.+?)\s*:?$', r'\1while \2:'),
            (r'^(\s*)berhenti\s*$', r'\1break'),
            (r'^(\s*)lanjut\s*$', r'\1continue'),
            
            # ==================== CLASS AND OOP ====================
            (r'^(\s*)kelas\s+(\w+)(?:\((.+)\))?\s*:?$', r'\1class \2(\3):'),
            (r'(\s*)diri\.', r'\1self.'),
            (r'(\s*)diri\b', r'\1self'),
            
            # ==================== EXCEPTION HANDLING ====================
            (r'^(\s*)coba\s*:?$', r'\1try:'),
            (r'^(\s*)kecuali\s*(.+?)?\s*:?$', r'\1except \2:'),
            (r'^(\s*)akhirnya\s*:?$', r'\1finally:'),
            (r'^(\s*)naikkan\s+(.+)$', r'\1raise \2'),
            
            # ==================== CONTEXT MANAGERS ====================
            (r'^(\s*)dengan\s+(.+?)\s+sebagai\s+(\w+)\s*:?$', r'\1with \2 as \3:'),
            
            # ==================== BOOLEAN AND NONE ====================
            (r'\bbenar\b', 'True'),
            (r'\bsalah\b', 'False'),
            (r'\bkosong\b', 'None'),
            (r'\bnull\b', 'None'),
            
            # ==================== LOGICAL OPERATORS ====================
            (r'\bdan\b', 'and'),
            (r'\batau\b', 'or'),
            (r'\btidak\b', 'not'),
            (r'\bdi\b', 'in'),
            (r'\badalah\b', 'is'),
            
            # ==================== LIST METHODS ====================
            (r'\.tambah\(', '.append('),
            (r'\.masukkan\(', '.insert('),
            (r'\.hapus\(', '.remove('),
            (r'\.bersihkan\(', '.clear('),
            (r'\.pop\(', '.pop('),
            (r'\.panjang\(\)', '.__len__()'),
            (r'\.index\(', '.index('),
            (r'\.urutkan\(', '.sort('),
            (r'\.balik\(', '.reverse('),
            (r'\.perluas\(', '.extend('),
            (r'\.salin\(\)', '.copy()'),
            
            # ==================== STRING METHODS ====================
            (r'\.jadikan_besar\(\)', '.upper()'),
            (r'\.jadikan_kecil\(\)', '.lower()'),
            (r'\.jadikan_kapital\(\)', '.capitalize()'),
            (r'\.jadikan_judul\(\)', '.title()'),
            (r'\.ganti\(', '.replace('),
            (r'\.pisah\(', '.split('),
            (r'\.gabung\(', '.join('),
            (r'\.strip\(', '.strip('),
            (r'\.lstrip\(', '.lstrip('),
            (r'\.rstrip\(', '.rstrip('),
            (r'\.cari\(', '.find('),
            (r'\.hitung\(', '.count('),
            (r'\.mulai_dengan\(', '.startswith('),
            (r'\.akhir_dengan\(', '.endswith('),
            (r'\.format\(', '.format('),
            
            # ==================== DICTIONARY METHODS ====================
            (r'\.ambil\(', '.get('),
            (r'\.kunci\(\)', '.keys()'),
            (r'\.nilai\(\)', '.values()'),
            (r'\.item\(\)', '.items()'),
            (r'\.perbarui\(', '.update('),
            (r'\.popitem\(\)', '.popitem()'),
        ]
        
        # Konteks global dengan semua fungsi bawaan
        self._global_context = {
            '__name__': '__main__',
            '__builtins__': builtins,
            'print': print,
            'input': input,
            'str': str,
            'int': int,
            'float': float,
            'bool': bool,
            'list': list,
            'dict': dict,
            'tuple': tuple,
            'set': set,
            'len': len,
            'range': range,
            'type': type,
            'sum': sum,
            'min': min,
            'max': max,
            'abs': abs,
            'round': round,
            'pow': pow,
            'enumerate': enumerate,
            'zip': zip,
            'map': map,
            'filter': filter,
            'sorted': sorted,
            'reversed': reversed,
            'open': open,
            'isinstance': isinstance,
            'issubclass': issubclass,
            'hasattr': hasattr,
            'getattr': getattr,
            'setattr': setattr,
            'delattr': delattr,
            'dir': dir,
            'id': id,
            'hash': hash,
            'chr': chr,
            'ord': ord,
            'hex': hex,
            'oct': oct,
            'bin': bin,
            'format': format,
            'repr': repr,
            'all': all,
            'any': any,
            'math': math,
            'random': random,
            'datetime': datetime,
            'json': json,
        }
        self.current_filename = None
        self.meta_lines = []
        self.python_lines = []
        self.line_mapping = {} 
        self.stats = {
            'files_processed': 0,
            'total_lines': 0,
            'execution_time': 0,
        }
    
    def _convert_list_comprehension(self, match):
        """Konversi list comprehension"""
        expr = match.group(1).strip()
        var = match.group(2)
        iterable = match.group(3)
        condition = match.group(4) if match.group(4) else None
        
        if condition:
            return f'[{expr} for {var} in {iterable} if {condition}]'
        else:
            return f'[{expr} for {var} in {iterable}]'
    
    def _convert_dict_comprehension(self, match):
        """Konversi dictionary comprehension"""
        expr = match.group(1).strip()
        var = match.group(2)
        iterable = match.group(3)
        condition = match.group(4) if match.group(4) else None
        
        if condition:
            return f'{{{expr} for {var} in {iterable} if {condition}}}'
        else:
            return f'{{{expr} for {var} in {iterable}}}'
    
    def parse(self, code: str) -> str:
        """
        Mengkonversi kode Meta Language ke Python
        """
        self.meta_lines = code.split('\n')
        hasil = ["# -*- coding: utf-8 -*-", "# Meta Language Generated Code"]
        self.line_mapping = {}
        
        for line_num, line in enumerate(self.meta_lines, 1):
            original_line = line
            comment_pos = -1
            in_string = False
            string_char = None
            
            for i, char in enumerate(line):
                if char in ('"', "'") and not in_string:
                    in_string = True
                    string_char = char
                elif char == string_char and in_string:
                    in_string = False
                    string_char = None
                elif char == '-' and i + 1 < len(line) and line[i:i+2] == '--' and not in_string:
                    comment_pos = i
                    break
            
            if comment_pos != -1:
                line = line[:comment_pos]
            
            if not line.strip():
                hasil.append('')
                self.line_mapping[len(hasil)] = line_num
                continue
            indent = ''
            for char in line:
                if char in (' ', '\t'):
                    indent += char
                else:
                    break
            
            stripped = line.strip()
            for pattern, replacement in self.konversi_rules:
                try:
                    if callable(replacement):
                        stripped = re.sub(pattern, replacement, stripped, flags=re.IGNORECASE | re.DOTALL)
                    else:
                        stripped = re.sub(pattern, replacement, stripped, flags=re.IGNORECASE | re.DOTALL)
                except Exception as e:
                    continue
            
            hasil.append(indent + stripped)
            self.line_mapping[len(hasil)] = line_num
        
        self.python_lines = hasil
        self.stats['total_lines'] += len(self.meta_lines)
        return '\n'.join(hasil)
    
    def _get_meta_line_number(self, python_lineno):
        """Mendapatkan nomor baris Meta dari nomor baris Python"""
        return self.line_mapping.get(python_lineno, python_lineno)
    
    def _wrap_execution(self, code: str, context: dict):
        """Wrapper untuk eksekusi dengan error handling yang lebih baik"""
        try:
            exec(code, context)
        except AttributeError as e:
            tb = sys.exc_info()[2]
            frame_summary = traceback.extract_tb(tb)[-1]
            python_lineno = frame_summary.lineno
            meta_lineno = self._get_meta_line_number(python_lineno)
            
            error_msg = str(e)
            if "object has no attribute" in error_msg:
                attr_name = error_msg.split("'")[1] if "'" in error_msg else "unknown"
                
                attr_mapping = {
                    '__len__': 'panjang',
                    'append': 'tambah',
                    'insert': 'masukkan',
                    'remove': 'hapus',
                    'clear': 'bersihkan',
                    'sort': 'urutkan',
                    'reverse': 'balik',
                    'extend': 'perluas',
                    'copy': 'salin',
                }
                
                meta_attr = attr_mapping.get(attr_name, attr_name)
                raise MetaAttributeError(f"Objek tidak memiliki method '{meta_attr}'", meta_lineno) from e
            raise MetaAttributeError(error_msg, meta_lineno) from e
        except NameError as e:
            tb = sys.exc_info()[2]
            frame_summary = traceback.extract_tb(tb)[-1]
            python_lineno = frame_summary.lineno
            meta_lineno = self._get_meta_line_number(python_lineno)
            
            var_name = str(e).split("'")[1] if "'" in str(e) else "unknown"
            raise MetaNameError(f"Variabel atau fungsi '{var_name}' tidak didefinisikan", meta_lineno) from e
        except TypeError as e:
            tb = sys.exc_info()[2]
            frame_summary = traceback.extract_tb(tb)[-1]
            python_lineno = frame_summary.lineno
            meta_lineno = self._get_meta_line_number(python_lineno)
            raise MetaTypeError(str(e), meta_lineno) from e
        except ZeroDivisionError as e:
            tb = sys.exc_info()[2]
            frame_summary = traceback.extract_tb(tb)[-1]
            python_lineno = frame_summary.lineno
            meta_lineno = self._get_meta_line_number(python_lineno)
            raise MetaZeroDivisionError("Tidak bisa membagi dengan nol", meta_lineno) from e
        except Exception as e:
            tb = sys.exc_info()[2]
            frame_summary = traceback.extract_tb(tb)[-1]
            python_lineno = frame_summary.lineno
            meta_lineno = self._get_meta_line_number(python_lineno)
            
            if not isinstance(e, (MetaError, MetaAttributeError, MetaNameError, MetaTypeError, MetaZeroDivisionError)):
                raise MetaRuntimeError(str(e), meta_lineno) from e
            raise
    
    def jalankan(self, filename: str, show_python: bool = False, args: List[str] = None, silent: bool = False) -> bool:
        """
        Menjalankan file Meta Language
        """
        import time
        start_time = time.time()
        
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                kode_meta = f.read() 
            self.current_filename = filename
            kode_python = self.parse(kode_meta)
            if show_python:
                self._tampilkan_hasil_konversi(kode_python, kode_meta)
            
            # Siapkan konteks eksekusi
            context = self._global_context.copy()
            if args:
                context['argv'] = args
                sys.argv = [filename] + args
            
            # Eksekusi kode dengan wrapper
            self._wrap_execution(kode_python, context)
            
            self.stats['files_processed'] += 1
            self.stats['execution_time'] += time.time() - start_time
            
            if not silent:
                print(f"\n✨ Program selesai dijalankan dalam {time.time() - start_time:.3f} detik")
            
            return True
            
        except FileNotFoundError:
            self._tampilkan_error(f"File '{filename}' tidak ditemukan")
            return False
        except SyntaxError as e:
            self._tampilkan_error_syntax(e, kode_meta if 'kode_meta' in locals() else None)
            return False
        except (MetaError, MetaAttributeError, MetaNameError, MetaTypeError, MetaZeroDivisionError, MetaRuntimeError) as e:
            self._tampilkan_error_meta(e)
            return False
        except Exception as e:
            self._tampilkan_error_runtime(e, kode_meta if 'kode_meta' in locals() else None, kode_python if 'kode_python' in locals() else None)
            return False
    
    def jalankan_string(self, code: str, show_python: bool = False) -> bool:
        """
        Menjalankan kode Meta Language dari string
        """
        import tempfile
        import time
        
        start_time = time.time()
        
        try:
            # Buat file temporary
            with tempfile.NamedTemporaryFile(mode='w', suffix='.meta', delete=False, encoding='utf-8') as f:
                f.write(code)
                temp_filename = f.name
            
            # Jalankan file temporary
            success = self.jalankan(temp_filename, show_python, silent=True)
            
            # Hapus file temporary
            try:
                os.unlink(temp_filename)
            except:
                pass
            
            return success
            
        except Exception as e:
            print(f"\n❌ Error: {str(e)}")
            return False
    
    def _tampilkan_hasil_konversi(self, kode_python: str, kode_meta: str):
        """Menampilkan kode Python hasil konversi dengan perbandingan"""
        print("\n" + "="*100)
        print(f"📜 DEBUG MODE - HASIL KONVERSI META KE PYTHON")
        print(f"📁 File: {self.current_filename}")
        print("="*100)
        
        # Tampilkan per baris
        meta_lines = kode_meta.split('\n')
        python_lines = kode_python.split('\n')
        
        print("\n{:^10} | {:^40} | {:^40}".format("Baris", "Meta Language", "Python"))
        print("-" * 100)
        
        max_lines = max(len(meta_lines), len(python_lines))
        for i in range(max_lines):
            meta_line = meta_lines[i] if i < len(meta_lines) else ""
            python_line = python_lines[i] if i < len(python_lines) else ""
            
            # Truncate if too long
            if len(meta_line) > 40:
                meta_line = meta_line[:37] + "..."
            if len(python_line) > 40:
                python_line = python_line[:37] + "..."
            
            print(f"{i+1:^10} | {meta_line:40} | {python_line:40}")
        
        print("\n" + "="*100)
        print("📝 KODE PYTHON LENGKAP:")
        print("="*100)
        print(kode_python)
        print("="*100 + "\n")
    
    def _tampilkan_error_syntax(self, error: SyntaxError, kode_asli: str):
        """Menampilkan error sintaks dengan detail dalam bahasa Meta"""
        print("\n" + "="*80)
        print(f"❌ ERROR SINTAKS - Meta Language")
        print(f"📁 File: {self.current_filename}")
        print("="*80)
        
        if hasattr(error, 'lineno') and error.lineno:
            meta_lineno = self._get_meta_line_number(error.lineno)
            print(f"\n📍 Lokasi: Baris {meta_lineno}")
            
            if self.meta_lines and meta_lineno <= len(self.meta_lines):
                baris_error = self.meta_lines[meta_lineno - 1]
                print(f"\n📝 Kode Meta yang bermasalah:")
                print(f"   {meta_lineno} | {baris_error}")
                
                if hasattr(error, 'offset') and error.offset:
                    print("   " + " " * (error.offset + 3) + "^")
                    pesan_meta = self._terjemahkan_pesan_error(error.msg)
                    print(f"   {pesan_meta}")
            
            print(f"\n🔍 Detail Error: {self._terjemahkan_pesan_error(error.msg)}")
            
            if self.meta_lines and meta_lineno <= len(self.meta_lines):
                self._beri_saran_detail(error, self.meta_lines[meta_lineno - 1])
        
        print("\n🔧 Tips:")
        print("   • Periksa tanda kurung (), {}, [] apakah berpasangan")
        print("   • Periksa tanda kutip '', \"\" apakah berpasangan")
        print("   • Pastikan indentasi konsisten (gunakan spasi atau tab)")
        print(f"   • Gunakan 'meta --debug {self.current_filename}' untuk melihat hasil konversi")
        print("="*80 + "\n")
    
    def _tampilkan_error_meta(self, error):
        """Menampilkan error Meta Language dengan pesan yang sudah diterjemahkan"""
        print("\n" + "="*80)
        print(f"❌ ERROR - Meta Language")
        print(f"📁 File: {self.current_filename}")
        print("="*80)
        
        error_type = type(error).__name__
        if error_type.startswith('Meta'):
            error_type = error_type[4:]
        
        print(f"\n📛 Tipe Error: {error_type}")
        
        meta_lineno = getattr(error, 'lineno', None)
        if meta_lineno:
            print(f"📍 Lokasi: Baris {meta_lineno}")
            
            if self.meta_lines and meta_lineno <= len(self.meta_lines):
                baris_meta = self.meta_lines[meta_lineno - 1]
                print(f"\n📝 Kode Meta yang bermasalah:")
                print(f"   {meta_lineno} | {baris_meta}")
                print("   " + "-" * (len(str(meta_lineno)) + 3 + len(baris_meta)))
        
        print(f"\n💬 Pesan: {str(error)}")
        
        self._tampilkan_saran_perbaikan(error)
        
        print("\n🔧 Tips Debugging:")
        print("   • Periksa baris yang disebutkan dalam error")
        print("   • Pastikan semua variabel sudah didefinisikan")
        print(f"   • Gunakan 'meta --debug {self.current_filename}' untuk lihat hasil konversi")
        print("="*80 + "\n")
    
    def _tampilkan_error_runtime(self, error: Exception, kode_asli: str, kode_python: str):
        """Menampilkan error runtime dengan pesan yang diterjemahkan"""
        print("\n" + "="*80)
        print(f"❌ ERROR RUNTIME - Meta Language")
        print(f"📁 File: {self.current_filename}")
        print("="*80)
        
        print(f"\n📛 Tipe Error: {type(error).__name__}")
        print(f"💬 Pesan: {self._terjemahkan_pesan_error(str(error))}")
        
        tb = traceback.extract_tb(sys.exc_info()[2])
        if tb:
            last_frame = tb[-1]
            if hasattr(last_frame, 'lineno'):
                python_lineno = last_frame.lineno
                meta_lineno = self._get_meta_line_number(python_lineno)
                print(f"\n📍 Lokasi: Baris {meta_lineno}")
                
                if self.meta_lines and meta_lineno <= len(self.meta_lines):
                    baris_meta = self.meta_lines[meta_lineno - 1]
                    print(f"\n📝 Kode Meta yang bermasalah:")
                    print(f"   {meta_lineno} | {baris_meta}")
        
        if "tidak memiliki method" in str(error).lower():
            print("\n💡 SARAN:")
            print("   Method yang Anda panggil tidak tersedia untuk tipe data tersebut.")
            print("   Periksa daftar method yang tersedia untuk tipe data yang digunakan.")
        
        if "tidak didefinisikan" in str(error).lower():
            print("\n💡 SARAN:")
            print("   Variabel atau fungsi tidak dikenal. Periksa:")
            print("   • Apakah Anda sudah mendefinisikan fungsi sebelum menggunakannya?")
            print("   • Apakah ada typo dalam nama variabel/fungsi?")
            print("   • Gunakan 'meta()' untuk output, 'masukan()' untuk input")
        
        if "membagi dengan nol" in str(error).lower():
            print("\n💡 SARAN:")
            print("   Anda mencoba membagi bilangan dengan nol.")
            print("   Tambahkan pengecekan sebelum operasi pembagian:")
            print("   jika penyebut != 0 maka:")
            print("       hasil = pembilang / penyebut")
        
        print("\n🔧 Tips Debugging:")
        print(f"   • Gunakan 'meta --debug {self.current_filename}' untuk lihat hasil konversi")
        print("   • Periksa baris yang disebutkan dalam error")
        print("   • Pastikan semua variabel sudah didefinisikan")
        print("="*80 + "\n")
    
    def _tampilkan_error(self, pesan: str, kode_asli: str = None):
        """Menampilkan error umum"""
        print("\n" + "="*80)
        print(f"❌ ERROR: {pesan}")
        if self.current_filename:
            print(f"📁 File: {self.current_filename}")
        print("="*80)
        print("\n🔧 Tips Debugging:")
        print("   • Gunakan 'meta --debug file.meta' untuk lihat hasil konversi")
        print("   • Pastikan file berekstensi .meta")
        print("   • Periksa sintaks program Anda")
        print("="*80 + "\n")
    
    def _tampilkan_saran_perbaikan(self, error):
        """Menampilkan saran perbaikan berdasarkan tipe error"""
        error_msg = str(error).lower()
        
        if "panjang" in error_msg and "method" in error_msg:
            print("\n💡 SARAN PERBAIKAN:")
            print("   Method '.panjang()' digunakan untuk mendapatkan panjang list/string")
            print("   ✅ Benar: buah.panjang()")
            print("   ❌ Salah: buah.panjang (tanpa kurung)")
            print("   ❌ Salah: panjang.buah()")
        
        elif "tidak didefinisikan" in error_msg:
            print("\n💡 SARAN PERBAIKAN:")
            print("   Variabel atau fungsi belum didefinisikan sebelum digunakan")
            print("   ✅ Periksa urutan penulisan kode")
            print("   ✅ Pastikan tidak ada typo pada nama variabel")
            print("   ✅ Definisi fungsi harus sebelum pemanggilan")
        
        elif "membagi dengan nol" in error_msg:
            print("\n💡 SARAN PERBAIKAN:")
            print("   Tambahkan pengecekan sebelum pembagian:")
            print("   jika penyebut != 0 maka:")
            print("       hasil = pembilang / penyebut")
            print("   selain itu:")
            print("       meta('Tidak bisa membagi dengan nol')")
        
        elif "indeks" in error_msg and "luar batas" in error_msg:
            print("\n💡 SARAN PERBAIKAN:")
            print("   Indeks yang diakses melebihi panjang list/string")
            print("   ✅ Periksa panjang data: data.panjang()")
            print("   ✅ Pastikan indeks dimulai dari 0")
            print("   ✅ Gunakan perulangan untuk akses yang aman")
    
    def _terjemahkan_pesan_error(self, pesan: str) -> str:
        """Menerjemahkan pesan error Python ke bahasa Indonesia"""
        terjemahan = {
            "invalid syntax": "sintaks tidak valid",
            "unexpected EOF while parsing": "akhir file tidak terduga saat parsing",
            "unterminated string literal": "string tidak ditutup dengan benar",
            "invalid decimal literal": "angka desimal tidak valid",
            "name 'masukan' is not defined": "fungsi 'masukan' tidak dikenal - pastikan menggunakan tanda kurung: masukan()",
            "name 'meta' is not defined": "fungsi 'meta' tidak dikenal - pastikan menggunakan tanda kurung: meta()",
            "list object has no attribute 'len'": "objek list tidak memiliki method 'panjang' - gunakan: list.panjang()",
            "object has no attribute": "objek tidak memiliki attribute",
            "is not defined": "tidak didefinisikan",
            "division by zero": "pembagian dengan nol",
            "list index out of range": "indeks list di luar batas",
            "string index out of range": "indeks string di luar batas",
            "expected an indented block": "diharapkan blok yang diindentasi",
        }
        
        for en, id in terjemahan.items():
            if en in pesan.lower():
                return id
        return pesan
    
    def _beri_saran_detail(self, error: SyntaxError, baris: str):
        """Memberikan saran detail berdasarkan error"""
        baris = baris.strip()
        
        if baris.count('(') != baris.count(')'):
            print("\n💡 Saran: Jumlah kurung buka '(' dan tutup ')' tidak sama")
            print(f"   Buka: {baris.count('(')}, Tutup: {baris.count(')')}")
        
        if baris.count('[') != baris.count(']'):
            print("\n💡 Saran: Jumlah kurung siku '[' dan ']' tidak sama")
            print(f"   Buka: {baris.count('[')}, Tutup: {baris.count(']')}")
        
        if baris.count('{') != baris.count('}'):
            print("\n💡 Saran: Jumlah kurung kurawal '{' dan '}' tidak sama")
            print(f"   Buka: {baris.count('{')}, Tutup: {baris.count('}')}")
        
        if baris.count('"') % 2 != 0 or baris.count("'") % 2 != 0:
            print("\n💡 Saran: Tanda kutip tidak berpasangan")
        
        if 'masukan' in baris and '(' not in baris:
            print("\n💡 Saran: Gunakan 'masukan()' dengan tanda kurung")
            print("   Contoh: nama = masukan('Masukkan nama: ')")
        
        if 'meta' in baris and '(' not in baris:
            print("\n💡 Saran: Gunakan 'meta()' dengan tanda kurung")
            print("   Contoh: meta('Hello World')")


# ==================== ERROR CLASSES ====================

class MetaError(Exception):
    """Base exception untuk Meta Language"""
    def __init__(self, message, lineno=None):
        super().__init__(message)
        self.lineno = lineno
    
    def __str__(self):
        if self.lineno:
            return f"[Baris {self.lineno}] {self.args[0]}"
        return self.args[0]


class MetaAttributeError(MetaError):
    def __init__(self, message, lineno=None):
        super().__init__(message, lineno)
        self.message = message
    
    def __str__(self):
        if self.lineno:
            return f"AttributeError pada baris {self.lineno}: {self.message}"
        return f"AttributeError: {self.message}"


class MetaNameError(MetaError):
    def __init__(self, message, lineno=None):
        super().__init__(message, lineno)
        self.message = message
    
    def __str__(self):
        if self.lineno:
            return f"NameError pada baris {self.lineno}: {self.message}"
        return f"NameError: {self.message}"


class MetaTypeError(MetaError):
    def __init__(self, message, lineno=None):
        super().__init__(message, lineno)
        self.message = message
    
    def __str__(self):
        if self.lineno:
            return f"TypeError pada baris {self.lineno}: {self.message}"
        return f"TypeError: {self.message}"


class MetaZeroDivisionError(MetaError):
    def __init__(self, message, lineno=None):
        super().__init__(message, lineno)
        self.message = message
    
    def __str__(self):
        if self.lineno:
            return f"ZeroDivisionError pada baris {self.lineno}: {self.message}"
        return f"ZeroDivisionError: {self.message}"


class MetaRuntimeError(MetaError):
    def __init__(self, message, lineno=None):
        super().__init__(message, lineno)
        self.message = message
    
    def __str__(self):
        if self.lineno:
            return f"RuntimeError pada baris {self.lineno}: {self.message}"
        return f"RuntimeError: {self.message}"


# ==================== MAIN FUNCTION ====================

def find_main_meta() -> Optional[str]:
    """Mencari file main.meta di direktori saat ini"""
    possible_files = ['main.meta', 'Main.meta', 'MAIN.meta', 'index.meta', 'app.meta']
    
    for file in possible_files:
        if os.path.exists(file):
            return file
    
    # Cek semua file .meta, jika hanya ada satu, gunakan itu
    meta_files = [f for f in os.listdir('.') if f.endswith('.meta')]
    if len(meta_files) == 1:
        return meta_files[0]
    
    return None


def tampilkan_bantuan():
    """Menampilkan bantuan"""
    bantuan = """
    ╔══════════════════════════════════════════════════════════════════════════════╗
    ║                          META LANGUAGE v1.0                                  ║
    ║                    Bahasa Pemrograman dengan Sintaks Indonesia               ║
    ╚══════════════════════════════════════════════════════════════════════════════╝
    
    PENGGUNAAN:
        meta                               - Menjalankan main.meta (auto-detect)
        meta <file.meta> [argumen...]      - Menjalankan program
        meta --debug [file.meta]           - Menjalankan dengan debug mode
        meta --repl                         - Mode interaktif (REPL)
        meta --help                        - Menampilkan bantuan ini
        meta --version                     - Menampilkan versi
    
    CONTOH:
        meta                               # Menjalankan main.meta
        meta program.meta                  # Menjalankan program.meta
        meta --debug program.meta          # Debug mode
        meta --repl                        # Mode interaktif
    
    CONTOH PROGRAM SEDERHANA:
    
    ----- main.meta -----
    meta("Hello World!")
    nama = masukan("Siapa nama Anda? ")
    meta(f"Halo, {nama}!")
    
    ----- kalkulator.meta -----
    meta("KALKULATOR SEDERHANA")
    a = desimal(masukan("Angka pertama: "))
    b = desimal(masukan("Angka kedua: "))
    hasil = a + b
    meta(f"Hasil: {a} + {b} = {hasil}")
    
    FUNGSI-FUNGSI YANG TERSEDIA:
    
    📝 INPUT/OUTPUT:
        meta("teks")      → Mencetak teks ke layar
        cetak("teks")     → Sama seperti meta()
        masukan("prompt") → Membaca input dari user
    
    🔢 TYPE CONVERSION:
        teks(123)         → "123"
        bilangan("456")   → 456
        desimal("3.14")   → 3.14
    
    ➗ MATEMATIKA:
        akar(16)          → 1.0
        pangkat(2,3)      → 8
        absolut(-5)       → 5
        bulatkan(3.7)     → 4
    
    🔀 PERCABANGAN:
        jika kondisi maka:
            # kode
        atau jika kondisi maka:
            # kode
        selain itu:
            # kode
    
    🔄 PERULANGAN:
        untuk item dalam list:
            # kode
        
        selama kondisi:
            # kode
    
    📚 LIST OPERATIONS:
        list.tambah(item)   → append
        list.panjang()      → len()
        list.urutkan()      → sort()
        list.balik()        → reverse()
    
    ══════════════════════════════════════════════════════════════════════════════
    """
    print(bantuan)


def repl_mode():
    """Mode REPL (Read-Eval-Print Loop) interaktif"""
    MetaBranding.print_logo_small()
    print("\n🔮 Meta Language REPL v1.0")
    print("   Ketik 'keluar' atau 'exit' untuk keluar")
    print("   Ketik '--debug' untuk toggle debug mode")
    print("-" * 50)
    
    interpreter = MetaInterpreter()
    debug_mode = False
    
    while True:
        try:
            # Prompt dengan warna (jika terminal mendukung)
            prompt = "🔷 meta> " if not debug_mode else "🔶 meta (debug)> "
            code = input(prompt).strip()
            
            if code.lower() in ['keluar', 'exit', 'quit']:
                print("👋 Sampai jumpa!")
                break
            
            if code == '--debug':
                debug_mode = not debug_mode
                print(f"🔧 Debug mode: {'AKTIF' if debug_mode else 'NONAKTIF'}")
                continue
            
            if not code:
                continue
            
            # Multi-line support
            if code.endswith(':'):
                lines = [code]
                while True:
                    line = input("... ").rstrip()
                    if not line:
                        break
                    lines.append(line)
                code = '\n'.join(lines)
            
            # Jalankan kode
            interpreter.jalankan_string(code, show_python=debug_mode)
            
        except KeyboardInterrupt:
            print("\n👋 Sampai jumpa!")
            break
        except EOFError:
            print("\n👋 Sampai jumpa!")
            break
        except Exception as e:
            print(f"❌ Error: {e}")


def main():
    """Fungsi utama untuk menjalankan interpreter"""
    
    # Setup branding (judul dan icon)
    MetaBranding.set_console_title("Meta Language v1.0")
    MetaBranding.set_console_icon()
    
    # Tanpa argumen: cari main.meta
    if len(sys.argv) == 1:
        main_file = find_main_meta()
        
        if main_file:
            MetaBranding.print_logo_small()
            print(f"\n🚀 Menjalankan: {main_file}\n")
            
            interpreter = MetaInterpreter()
            success = interpreter.jalankan(main_file)
            
            if not success:
                sys.exit(1)
        else:
            MetaBranding.print_banner()
            print("\n❌ Tidak ada file .meta yang ditemukan!")
            print("\n📋 Cara penggunaan:")
            print("   meta                     # Menjalankan main.meta")
            print("   meta program.meta        # Menjalankan program.meta")
            print("   meta --repl              # Mode interaktif")
            print("   meta --help              # Bantuan lengkap")
            
            # Tawarkan untuk membuat main.meta
            print("\n💡 Ingin membuat file main.meta contoh? (y/n): ", end='')
            try:
                response = input().strip().lower()
                if response == 'y':
                    create_example_file()
            except:
                pass
            
            sys.exit(1)
        
        return
    
    # Proses argumen
    if sys.argv[1] == '--repl':
        repl_mode()
        return
    
    if sys.argv[1] == '--version' or sys.argv[1] == '-v':
        print("Meta Language v1.0")
        print("Bahasa Pemrograman dengan Sintaks Indonesia")
        return
    
    if sys.argv[1] == '--help' or sys.argv[1] == '-h':
        tampilkan_bantuan()
        return
    
    interpreter = MetaInterpreter()
    
    # Debug mode
    if sys.argv[1] == '--debug':
        if len(sys.argv) < 3:
            # Coba cari main.meta
            main_file = find_main_meta()
            if main_file:
                filename = main_file
            else:
                print("\n❌ ERROR: Tidak ada file yang ditentukan dan tidak ada main.meta")
                print("\nPenggunaan: meta --debug <file.meta>")
                sys.exit(1)
        else:
            filename = sys.argv[2]
        
        if not filename.endswith('.meta'):
            print(f"\n❌ ERROR: File '{filename}' harus berekstensi .meta")
            sys.exit(1)
        
        if not os.path.exists(filename):
            print(f"\n❌ ERROR: File '{filename}' tidak ditemukan")
            sys.exit(1)
        
        MetaBranding.print_logo_small()
        print(f"\n🔧 DEBUG MODE - File: {filename}\n")
        
        success = interpreter.jalankan(filename, show_python=True, args=sys.argv[3:])
        if not success:
            sys.exit(1)
    
    else:
        filename = sys.argv[1]
        
        if not filename.endswith('.meta'):
            print(f"\n❌ ERROR: File '{filename}' harus berekstensi .meta")
            sys.exit(1)
        
        if not os.path.exists(filename):
            print(f"\n❌ ERROR: File '{filename}' tidak ditemukan")
            sys.exit(1)
        
        MetaBranding.print_logo_small()
        print(f"\n🚀 Menjalankan: {filename}\n")
        
        success = interpreter.jalankan(filename, show_python=False, args=sys.argv[2:])
        if not success:
            sys.exit(1)


def create_example_file():
    """Membuat file main.meta contoh"""
    example_code = '''-- main.meta
-- Contoh program Meta Language

meta("╔══════════════════════════════════════╗")
meta("║     SELAMAT DATANG DI META LANGUAGE  ║")
meta("╚══════════════════════════════════════╝")
meta("")

-- Input nama
nama = masukan("Siapa nama Anda? ")

-- Sapaan
meta(f"Halo, {nama}! Selamat belajar Meta Language!")
meta("")

-- Contoh kalkulator sederhana
meta("=== KALKULATOR SEDERHANA ===")
a = desimal(masukan("Masukkan angka pertama: "))
b = desimal(masukan("Masukkan angka kedua: "))

meta(f"{a} + {b} = {a + b}")
meta(f"{a} - {b} = {a - b}")
meta(f"{a} × {b} = {a * b}")

jika b != 0 maka:
    meta(f"{a} ÷ {b} = {a / b}")
selain itu:
    meta("Tidak bisa membagi dengan nol!")

meta("")
meta("=== CONTOH LIST ===")
buah = ["apel", "jeruk", "mangga"]
meta("List buah:", buah)
meta("Jumlah buah:", buah.panjang())
buah.tambah("anggur")
meta("Setelah tambah anggur:", buah)

meta("")
meta("=== CONTOH PERULANGAN ===")
untuk i dalam rentang(1, 6):
    meta(f"Angka ke-{i}")

meta("")
meta("Terima kasih telah menggunakan Meta Language! 🚀")
'''
    
    with open('main.meta', 'w', encoding='utf-8') as f:
        f.write(example_code)
    
    print("\n✅ File main.meta telah dibuat!")
    print("🚀 Jalankan dengan perintah: meta")
    print("🔧 Atau debug mode: meta --debug")


if __name__ == '__main__':
    main()