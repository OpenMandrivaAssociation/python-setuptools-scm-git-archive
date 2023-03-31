# Created by pyp2rpm-3.3.1
%global pypi_name setuptools-scm-git-archive

Name:           python-%{pypi_name}
Version:        1.4
Release:        2
Summary:        setuptools_scm plugin for git archives
Group:          Development/Python
License:        MIT
URL:            https://github.com/Changaco/setuptools_scm_git_archive/
Source0:        https://files.pythonhosted.org/packages/source/s/%{pypi_name}/setuptools_scm_git_archive-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python-devel
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(setuptools-scm)
Requires:       python3dist(setuptools)

%description
This is a setuptools_scm plugin that adds support for git archives (for
example the ones GitHub automatically generates). Note that it only works for
archives of tagged commits (because git currently lacks a format option
equivalent to git describe --tags).

%prep
%autosetup -n setuptools_scm_git_archive-%{version}

# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py_build

%install
# Must do the default python version install last because
# the scripts in /usr/bin are overwritten with every setup.py install.
%py_install

%files
%license LICENSE
%doc README.rst
%{python_sitelib}/setuptools_scm_git_archive/
%{python_sitelib}/setuptools_scm_git_archive-*-py*.*.egg-info/
