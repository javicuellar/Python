import 'package:flutter/material.dart';

import '../flet_control_backend.dart';
import '../models/control.dart';
import '../utils/colors.dart';
import '../utils/debouncer.dart';
import '../utils/edge_insets.dart';
import '../utils/mouse.dart';
import '../utils/others.dart';
import '../utils/platform.dart';
import 'create_control.dart';
import 'cupertino_slider.dart';
import 'flet_store_mixin.dart';

class SliderControl extends StatefulWidget {
  final Control? parent;
  final Control control;
  final bool parentDisabled;
  final bool? parentAdaptive;
  final FletControlBackend backend;

  const SliderControl(
      {super.key,
      this.parent,
      required this.control,
      required this.parentDisabled,
      required this.parentAdaptive,
      required this.backend});

  @override
  State<SliderControl> createState() => _SliderControlState();
}

class _SliderControlState extends State<SliderControl> with FletStoreMixin {
  double _value = 0;
  final _debouncer = Debouncer(milliseconds: isDesktopPlatform() ? 10 : 100);
  late final FocusNode _focusNode;

  @override
  void initState() {
    super.initState();
    _focusNode = FocusNode();
    _focusNode.addListener(_onFocusChange);
  }

  @override
  void dispose() {
    _debouncer.dispose();
    _focusNode.removeListener(_onFocusChange);
    _focusNode.dispose();
    super.dispose();
  }

  void _onFocusChange() {
    widget.backend.triggerControlEvent(
        widget.control.id, _focusNode.hasFocus ? "focus" : "blur");
  }

  void onChange(double value) {
    var svalue = value.toString();
    debugPrint(svalue);
    _value = value;
    var props = {"value": svalue};
    widget.backend.updateControlState(widget.control.id, props, server: false);
    _debouncer.run(() {
      widget.backend.updateControlState(widget.control.id, props);
      widget.backend.triggerControlEvent(widget.control.id, "change");
    });
  }

  @override
  Widget build(BuildContext context) {
    debugPrint("SliderControl build: ${widget.control.id}");
    bool disabled = widget.control.isDisabled || widget.parentDisabled;
    return withPagePlatform((context, platform) {
      bool? adaptive =
          widget.control.attrBool("adaptive") ?? widget.parentAdaptive;
      if (adaptive == true &&
          (platform == TargetPlatform.iOS ||
              platform == TargetPlatform.macOS)) {
        return CupertinoSliderControl(
            control: widget.control,
            parentDisabled: widget.parentDisabled,
            backend: widget.backend);
      }

      String? label = widget.control.attrString("label");

      double min = widget.control.attrDouble("min", 0)!;
      double max = widget.control.attrDouble("max", 1)!;
      int round = widget.control.attrInt("round", 0)!;

      double value = widget.control.attrDouble("value", min)!;
      if (_value != value) {
        // verify limits
        if (value < min) {
          _value = min;
        } else if (value > max) {
          _value = max;
        } else {
          _value = value;
        }
      }

      var slider = Slider(
          autofocus: widget.control.attrBool("autofocus", false)!,
          focusNode: _focusNode,
          value: _value,
          min: min,
          max: max,
          year2023: widget.control.attrBool("year2023"),
          divisions: widget.control.attrInt("divisions"),
          label: label?.replaceAll("{value}", _value.toStringAsFixed(round)),
          activeColor: widget.control.attrColor("activeColor", context),
          inactiveColor: widget.control.attrColor("inactiveColor", context),
          overlayColor: parseWidgetStateColor(
              Theme.of(context), widget.control, "overlayColor"),
          allowedInteraction:
              parseSliderInteraction(widget.control.attrString("interaction")),
          thumbColor: widget.control.attrColor("thumbColor", context),
          padding: parseEdgeInsets(widget.control, "padding"),
          onChanged: !disabled
              ? (double value) {
                  onChange(value);
                }
              : null,
          mouseCursor:
              parseMouseCursor(widget.control.attrString("mouseCursor")),
          secondaryActiveColor:
              widget.control.attrColor("secondaryActiveColor", context),
          secondaryTrackValue: widget.control.attrDouble("secondaryTrackValue"),
          onChangeStart: !disabled
              ? (double value) {
                  widget.backend.triggerControlEvent(
                      widget.control.id, "change_start", value.toString());
                }
              : null,
          onChangeEnd: !disabled
              ? (double value) {
                  widget.backend.triggerControlEvent(
                      widget.control.id, "change_end", value.toString());
                }
              : null);

      return constrainedControl(context, slider, widget.parent, widget.control);
    });
  }
}
